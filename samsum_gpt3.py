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
    openai.api_key = '' #need API key here
    setting=args.setting
    mode=args.mode

    plm_name='gpt3'
    data_path=args.data_path
    if 'samsum' in data_path:
        dst = 'samsum'
    elif 'dialogsum' in data_path:
        dst = 'dialogsum'

    output_path = '{}_{}_chain_{}_{}.txt'.format(plm_name, dst,setting,str(mode))
    with open('samsum_topic.txt','r',encoding='utf8') as f:
        datas=f.readlines()

    topics=[data.strip().lower() for data in datas]


    with open(args.data_path, 'r', encoding='utf8') as f, \
            open(output_path, 'w', encoding='utf8') as of:
        data = f.readlines()[:]
        lines = []
        for i in data:
            d = json.loads(i)
            dialogue = d['dialogue']
            lines.append('[Dialogue]: '+dialogue)


        for idx, line in tqdm(enumerate(lines)):
            sent = line.strip()
            topic= topics[idx]
            prefix, postfix = prompting(args,setting, sent, mode,topic)

            prompt = prefix + str(sent) + "\n\n"+postfix
            # input_ids = wordpunct_tokenize(prompt)
            max_len = 50
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
    parser.add_argument("--data_path", type=str, default='/Users/guoqingluo/Desktop/PromptSum/data/ori_samsum/test.jsonl')
    parser.add_argument('--moshi', default='train', type=str)
    parser.add_argument('--setting', default='5shot', type=str)
    parser.add_argument('--mode', default='num_name_topic', type=str)
    args = parser.parse_args()
    print("let's start")
    if args.moshi == "train":
        main(args)