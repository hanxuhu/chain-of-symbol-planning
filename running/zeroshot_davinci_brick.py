import os
from time import sleep
import openai
import json
openai.api_key ="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"#os.getenv("OPENAI_API_KEY")
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
        default='shuffle_both',
        help="setting",
    )

parser.add_argument(
        "--num",
        type=str,
        default='1',
        help="num",
    )

parser.add_argument(
        "--model_name",
        type=str,
        default='chatgpt',
        help="num",
    )

args = parser.parse_args()


import json

prompt_type = args.prompt_type
setting = args.setting
if args.setting == 'noshuffle':
   setting = 'shuffle_descpt'
#prompt = open('demo/{}_demo_{}_{}.txt'.format(prompt_type,setting, args.num)).read()
#cot_prompt_1d = open('demo/davinci_cos_1d.txt').read()
#base_prompt = open('demo/baseline_demo.txt').read()
model_name = args.model_name
print('model name: ', model_name)
# Opening JSON file
f = open('data/brick_2d/{}_2d.json'.format(args.setting))
data = json.load(f)
zeroshot_brick_prompt = 'Lets think step by step, and provide the answer in the format of a sequence of bricks by a comma in the last sentence.'
res_list = []
res_label = []
i = 0
step = 0

for item in data:
   while 1:
      try:
         step +=1
         if step%10==0:
            print(step)
         if model_name == 'text-davinci-003':
           response = openai.Completion.create(
            model=model_name,
            prompt=  'Question:' + '\n' + item['data'] + zeroshot_brick_prompt+ 'Answer:\n',#cos_prompt_1d  + '\n' +  'Story:' + '\n' +  item['story'] + '\n'+"Question:" +  '\n'+ item['question'] + '?',
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
              {"role": "user", "content":  'Question:' + '\n' + item['data'] + '\n' + zeroshot_brick_prompt+'\nAnswer:\n',
              }
            ]
           )
         break
      except:
         print('error')
         sleep(5)
        
  
   if model_name == 'text-davinci-003':
       res = response['choices'][0]['text']
   else:
       res = response['choices'][0]['message']['content']
   dict_res = {'pred':res, 'label': item['label']}
   #res_label.append(item['label'])
   res_list.append(dict_res)
   #print(dict_res)
   #sleep(3)
   #res_final = {res_list}
if model_name == 'text-davinci-003':
    file_txt = 'davinci003_results/brick_{}_zeroshot.json'.format(args.setting)
    with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)
else:
   file_txt = 'chatgpt_results/brick2d_{}_zeroshot.json'.format(args.setting)
   with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)






