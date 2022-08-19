# CoI
Chain-of-Information prompting

## Requirements

Python>=3.6

Pytorch==1.10.2

bertscore==0.3.8

pyrouge


## Model downloading

We use Eleuther AI's [gpt-j-6B](https://huggingface.co/EleutherAI/gpt-j-6B/tree/main) and [gpt-Neo-1.3B](https://huggingface.co/EleutherAI/gpt-neo-1.3B/tree/main)

We use [OpenAI API](https://openai.com/api/pricing/) to run GPT-3.

Please also download [gpt2](https://huggingface.co/gpt2/tree/main) as the tokenizer to run the model.

## Model running

Take gpt-neo-1.3B as an example. Run the model:

```
bash run_gptneo.sh
```

Copy the first four lines of ``run_gptneo.sh`` into ``process.py``, and run:
```
python3 process.py
```

## Evaluation

Copy the first four lines of ``run_gptneo.sh`` into ``eval.sh``, and run:
```
bash eval.sh
```