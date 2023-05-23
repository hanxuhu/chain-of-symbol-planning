# Chain-of-Symbol Prompting Elicits Planning in Large Language Models



Code and data of paper: _Chain-of-Symbol Prompting Elicits Planning in Large Language Models_. 2023

Hanxu Hu. Westlake Unversity

[Paper pdf](https://arxiv.org/pdf/2305.10276.pdf)

> We take the initiative to investigate the performance of LLMs on complex planning tasks that require LLMs to understand a virtual spatial environment simulated via natural language and act correspondingly in text. We propose a benchmark named Natural Language Planning (NLP) composed of a set of novel tasks: Brick World, NLVR-based Manipulations, and Natural Language Navigation. We found that current popular LLMs such as ChatGPT still lack abilities in complex planning. This arises a question -- do the LLMs have a good understanding of the environments described in natural language, or maybe other alternatives such as symbolic representations are neater and hence better to be understood by LLMs? To this end, we propose a novel method called CoS (Chain-of-Symbol Prompting) that represents the complex environments with condensed symbolic spatial representations during the chained intermediate thinking steps. CoS is easy to use and does not need additional training on LLMs. Extensive experiments indicate that CoS clearly surpasses the performance of the Chain-of-Thought (CoT) Prompting in all three planning tasks with even fewer tokens used in the inputs compared with CoT on ChatGPT and InstructGPT. The performance gain is strong, by up to 60.8% accuracy (from 31.8% to 92.6%) on Brick World for ChatGPT. CoS also reduces the number of tokens in the prompt obviously, by up to 65.8% of the tokens (from 407 to 139) for the intermediate steps from demonstrations on Brick World.

## Quickstart
```bash
pip install -r requirements.txt
```

```bash
api_key=<YOUR_OPENAI_API_KEY>
cd running;
python test_brick.py\
   --prompt_type "cos"\
   --num 5\
   --setting "shuffle_both"\
   --model_name "chatgpt"\
   --key ${api_key}

```
This is to use chatgpt with Chain-of-Symbol (CoS) prompting in Brick World 1d task, and in "shuffle both" setting.
The outputs will be saved in "results/chatgpt_results/". 

or you can also adjust the parameters in test_brick.sh, then:
```bash
bash test_brick.sh
```

For NLVR-based Manipunation:
firstly change the api key in test_navigation_nlvr.sh, then:
```bash
bash test_navigation_nlvr.sh
```


## Evaluation
You can do evaluation direclty:

```bash
cd eval;
python eval_prompt.py;
python eval_nlvr.py;
python eval_navigation.py;
```
## Data

We have created the data of Brick World, NVLR-based Manipunation, and Natural Language Planning in you can view them through:
```bash
cd data
```
You can also costomize your own Natural Language Planning data by modifying 'create_bricks.py', 'create_navigate.py', and 'create_nlvr.py' and run them.
