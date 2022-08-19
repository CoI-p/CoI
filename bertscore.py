import bert_score
import argparse
import logging
import transformers
import codecs
transformers.tokenization_utils.logger.setLevel(logging.ERROR)
transformers.configuration_utils.logger.setLevel(logging.ERROR)
transformers.modeling_utils.logger.setLevel(logging.ERROR)

from bert_score import score

def eval(c,r):
    with open(c,'r') as f:
        cands = [line.strip() for line in f]

    with open(r,'r') as f:
        refs = [line.strip() for line in f]

    P, R, F1 = score(cands, refs, lang='en', verbose=True,model_type="microsoft/deberta-xlarge-mnli")
    print(f"System level F1 score: {F1.mean():.3f}")

parser = argparse.ArgumentParser()
parser.add_argument('--c', type=str, default="data/test/gpt3_chain_1shot_name.txt",
                    help='candidate file')
parser.add_argument('--r', type=str, default="data/test/dialogsum.test.ref.txt",
                    help='reference file')
args = parser.parse_args()

eval(args.c,args.r)


