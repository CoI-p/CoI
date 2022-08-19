plm='gpt-neo-1.3B'
dst='dialogsum'
setting='5shot'
mode='num_name_topic'

CUDA_VISIBLE_DEVICES=2 python3 summarization.py --data_path data/${dst}/test.jsonl --setting ${setting} --mode ${mode} --class_name EleutherAI/${plm}

