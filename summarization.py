import argparse
import json
import os.path

import torch
from tqdm import tqdm
from transformers import GPTNeoForCausalLM, AutoModelForCausalLM,AutoTokenizer
from functions import prompting

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

parser = argparse.ArgumentParser(description="model parameters")
parser.add_argument('--class_name',default='EleutherAI/gpt-neo-1.3B',type=str)
# parser.add_argument('--class_name',default='gpt2',type=str)
parser.add_argument('--mode',default='None',type=str)
parser.add_argument('--setting',default='5shot',type=str)

parser.add_argument("--data_path",type=str, default='data/dialogsum/test.jsonl')
args=parser.parse_args()
class_name=args.class_name
mode = args.mode
setting = args.setting


if 'samsum' in args.data_path:
    dst='samsum'
elif 'dialogsum' in args.data_path:
    dst='dialogsum'


plm_name=class_name.split('/')[1]
if 'gpt-j-hf' in class_name:
    plm = GPTNeoForCausalLM.from_pretrained(class_name)
    plm.half()
else:
    plm = AutoModelForCausalLM.from_pretrained(class_name)
    plm.half()

plm.eval()
plm.to(device)
tokenizer = AutoTokenizer.from_pretrained('gpt2')
tokenizer.pad_token = tokenizer.eos_token

def run():

    output_path = '{}_{}_chain_{}_{}.txt'.format(plm_name, dst,setting, str(mode))

    with open(output_path, 'w', encoding='utf8') as of, \
            open(args.data_path, 'r', encoding='utf8') as f:
        data = f.readlines()[:]
        lines = []
        topics = []
        for i in data:
            d = json.loads(i)
            dialogue = d['dialogue']
            lines.append('[Dialogue]:' + dialogue)
            if dst=='dialogsum':
                topic =d['topic1']
                topics.append(topic)

        for idx,line in tqdm(enumerate(lines)):
            sent = line.strip()
            if dst=='samsum':
                topic=None
            else:
                topic= topics[idx]
            prefix, postfix = prompting(args,setting,line,mode,topic)

            sent=' '.join(sent.split()[:512])
            prompt = prefix + str(sent) + "\n\n" + postfix
            input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
            max_len = len(input_ids[0])+50

            gen_tokens = plm.generate(
                input_ids,
                do_sample=True,
                temperature=0.7,
                max_length=max_len,
                pad_token_id=tokenizer.eos_token_id
            )
            gen_text = tokenizer.batch_decode(gen_tokens)[0]
            if setting=='zero-shot':
                written_text=''.join(''.join(gen_text.split(sent)[1:]).split('\n'))
            elif setting=='1shot':
                written_text=''.join(''.join(gen_text.split('To summarize: ')[2:3]).split('\n'))
            elif setting=='2shot':
                written_text=''.join(''.join(gen_text.split('To summarize: ')[3:4]).split('\n'))
            elif setting == '3shot':
                written_text = ''.join(''.join(gen_text.split('To summarize: ')[4:5]).split('\n'))
            elif setting == '4shot':
                written_text = ''.join(''.join(gen_text.split('To summarize: ')[5:6]).split('\n'))
            elif setting=='5shot':
                written_text = ''.join(gen_text.split('To summarize: ')[6:7]).split('\n')[0]
            if len(written_text) <= 7:
                written_text = '<|endoftext|>'
            of.write('Generated:\n')
            of.write(written_text+'\n\n')
            of.flush()


def main():
    run()

if __name__ == '__main__':
    main()
