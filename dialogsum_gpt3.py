import json
import openai
import gpt
import numpy as np
import pandas as pd
import argparse
from nltk import wordpunct_tokenize
from tqdm import tqdm
from functions import prompting

def main(args):
    openai.api_key = '' # need API here
    setting=args.setting
    mode=args.mode

    plm_name='gpt3'
    data_path=args.data_path
    if 'samsum' in data_path:
        dst = 'samsum'
    elif 'dialogsum' in data_path:
        dst = 'dialogsum'

    output_path = '{}_{}_chain_{}_{}.txt'.format(plm_name, dst,setting,str(mode))

    with open(args.data_path, 'r', encoding='utf8') as f, \
            open(output_path, 'w', encoding='utf8') as of:
        data = f.readlines()[:]
        lines = []
        topics= []
        for i in data:
            d = json.loads(i)
            dialogue = d['dialogue']
            topic =d['topic1']
            lines.append('[Dialogue]:'+dialogue)
            topics.append(topic)

        for idx, line in tqdm(enumerate(lines)):
            sent = line.strip()
            topic= topics[idx]
            prefix, postfix = prompting(args,setting, sent, mode,topic)

            prompt = prefix + str(sent) + "\n\n"+postfix

            max_len = 48
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=max_len,
                temperature=0.7)

            content1 = response.choices[0].text.strip()

            of.write("Generated:\n")
            of.write(content1+"\n\n")
            of.flush()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, default='./data/dialogsum/test.jsonl')
    parser.add_argument('--moshi', default='train', type=str)
    parser.add_argument('--setting', default='5shot', type=str)
    parser.add_argument('--mode', default='topic', type=str)
    args = parser.parse_args()
    print("let's start")
    if args.moshi == "train":
        main(args)