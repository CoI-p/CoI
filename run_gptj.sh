plm='gpt-j-6B'
dst='dialogsum'
setting='5shot'
mode='None'

CUDA_VISIBLE_DEVICES=2 python3 summarization.py --data_path data/${dst}/test.jsonl --setting ${setting} --mode ${mode} --class_name EleutherAI/${plm}



