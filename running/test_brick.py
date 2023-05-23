import os
from time import sleep
import openai
import json

import argparse
def process(response):
  print(response)
  json_object = json.dumps(response["choices"][0]["message"]["content"], ensure_ascii=False).encode('utf8')
  print(json_object.decode())
  return json_object.decode()
parser = argparse.ArgumentParser(description="test LLM planning abilities")
parser.add_argument(
        "--prompt_type",
        type=str,
        default='cos',
        help="type of prompt",
    )

parser.add_argument(
        "--setting",
        type=str,
        default='shuffle_descpt',
        help="setting",
    )

parser.add_argument(
        "--num",
        type=str,
        default='2',
        help="num",
    )
parser.add_argument(
        "--model_name",
        type=str,
        default='chatgpt',
        help="num",
    )

parser.add_argument(
        "--key",
        type=str,
        default='xxx',
        help="num",
    )
args = parser.parse_args()
openai.api_key = args.key

import json

prompt_type = args.prompt_type
setting = args.setting
if args.setting == 'noshuffle':
   setting = 'shuffle_descpt'
prompt = open('../demo/{}_demo_{}_2.txt'.format(prompt_type,args.setting)).read()
#cot_prompt_1d = open('demo/davinci_cos_1d.txt').read()
#base_prompt = open('demo/baseline_demo.txt').read()
model_name = args.model_name
# Opening JSON file
f = open('../data/brick1d_data/data_brick_{}.json'.format(args.setting))
zeroshot_prompt = 'Lets think step by step, and provide the answer in the format of a sequence of bricks by a comma in the last sentence.'
data = json.load(f)
res_list = []
res_label = []
constraint_prompt = 'You only need to return the sequence of removed bricks in order from top to bottom, without any explaination. So the answer is:'
cos_1d_desc = "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n" #+Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"},
i = 0
step = 0

for item in data:
   error_list = []
   while 1:
      try:
         step +=1
         if step%10==0:
            print(step)
         if model_name == 'text-davinci-003':
           response = openai.Completion.create(
            model=model_name,
            prompt= prompt + '\n\n' + 'Question:' + '\n' + item['data'] + 'Answer:\n',#cos_prompt_1d  + '\n' +  'Story:' + '\n' +  item['story'] + '\n'+"Question:" +  '\n'+ item['question'] + '?',
            temperature=0,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
           )
         else:
           response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=2048,
            temperature=0,
            messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": prompt+ '\n\n' + 'Question:' + '\n' + item['data'] + '\nAnswer:\n',
              }
            ]
           )
         if model_name == 'text-davinci-003':
             res = response['choices'][0]['text']
         else:
             res = response['choices'][0]['message']['content']
         dict_res = {'pred':res, 'label': item['label']}
           #res_label.append(item['label'])
         res_list.append(dict_res)
         break
      except:
         print('error')
         sleep(5)
         error_list.append('error')
         if len(error_list)>3:
            break

        
  
   
   #print(dict_res)
   #sleep(3)
   #res_final = {res_list}
if model_name == 'text-davinci-003':
    file_txt = '../results/davinci003_results/brick/{}_{}_results.json'.format(args.setting, prompt_type)
    with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)
else:
   file_txt = '../results/chatgpt_results/brick_{}_5shot_{}_{}.json'.format(args.setting, prompt_type, args.num)
   with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)




