plm='gpt-neo-1.3B'
dst='dialogsum'
setting='5shot'
mode='num_name_topic'

cands=${plm}_chain_${setting}_${mode}.txt
refs=./data/test/${dst}.test.ref.txt

CUDA_VISIBLE_DEVICES=0 python3 test_rouge.py --c ${cands} --r ${refs}
CUDA_VISIBLE_DEVICES=0 bert-score -c ${cands} -r ${refs} --lang en --rescale_with_baseline