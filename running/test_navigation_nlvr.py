import os
from time import sleep
import openai
import json
#openai.api_key ="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"#os.getenv("OPENAI_API_KEY")

def process(response):
  print(response)
  json_object = json.dumps(response["choices"][0]["message"]["content"], ensure_ascii=False).encode('utf8')
  print(json_object.decode())
  return json_object.decode()

import argparse
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
        default='nlvr',
        help="setting",
    )

parser.add_argument(
        "--num",
        type=str,
        default='1',
        help="num",
    )

parser.add_argument(
        "--key",
        type=str,
        default="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",
        help="api key",
    )

parser.add_argument(
        "--model_name",
        type=str,
        default='text-davinci-003',
        help="num",
    )

parser.add_argument(
        "--zero_shot",
        type=bool,
        default=False,
        help="whether zeroshot",
    )

args = parser.parse_args()
openai.api_key = args.key
print('model_name', args.model_name)
print('api key', args.key)
print('num', args.num)
print('prompt', args.prompt_type)
print('zero shot', args.zero_shot)
import json
#cot_prompt = open('demo/cot_demo_1.txt').read()
prompt = open('../demo/{}_{}_{}.txt'.format(args.setting, args.prompt_type, args.num)).read()# cot_prompt = open('demo/navigation_cot_{}.txt').read()
zero_shot_prompt_navigation = "Let's think step by step, and provide the answer as the format of sequence of landmarks seperated by comma in the last sentence."
zero_shot_prompt_nlvr = "Let's think step by step, and provide the answer as the format of sequence of objects seperated by comma in the last sentence."
model_name = args.model_name
# Opening JSON file
if args.setting == 'nlvr':
   path = '../data/nlvr_data/nlvr_data.json'
else:
   path = '../data/navigation/navigation_data.json'
f = open(path)

data = json.load(f)
res_list = []
res_label = []
i = 0
step = 0
for i in range(1):
  
  res_list = []
  for item in data:
   #print(item['Story'])
   step +=1
   #if step%50==0:
   print(step)
   #print(step)
   if args.setting == 'navigation':
     if args.zero_shot==True:
       nput_text =  item['Story'] + '\n'+ item['Question'] + '\n' + zero_shot_prompt_navigation  +'\n'
     else:
       input_text = prompt + '\n\n'  + item['Story'] + '\n' + item['Question'] 
   else:
     if args.zero_shot==True:
       nput_text =  item['story'] + '\n'+ item['question'] + '\n' + zero_shot_prompt_navigation + '\n'
     else:
       input_text = prompt + '\n\n' + 'Story:' + '\n' + item['story'] + '\n' +'Question:'+ item['question'] + '\nAnswer:\n'
      
   while 1:
      try:
        if model_name == 'text-davinci-003':
           response = openai.Completion.create(
            model=model_name,
            prompt= input_text,#cos_prompt_1d  + '\n' +  'Story:' + '\n' +  item['story'] + '\n'+"Question:" +  '\n'+ item['question'] + '?',
            temperature=0,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
           )

        else:
           response = openai.ChatCompletion.create(
            #response = openai.Completion.create(
            model= "gpt-3.5-turbo",
            #model="text-davinci-003",
            max_tokens=2048,
            temperature=0,
            messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text, #item['Story'] +  '\n'+ item['Question'] + '\n' + zero_shot_prompt ,  #cos_prompt + '\n\n' + item['Story'] +  '\n'+ item['Question']
            }]
          )
        break
      except:
        print("error")
        sleep(5)
        #break

   if model_name == 'text-davinci-003':
       res = response['choices'][0]['text']
   else:
       res = response['choices'][0]['message']['content']
   dict_res = {'pred':res, 'label': item['Answer']}
   #res_label.append(item['label'])
   res_list.append(dict_res)
   #print(dict_res)
   #sleep(3)
   #res_final = {res_list}
  if model_name == 'text-davinci-003':
    file_txt = '../results/davinci003_results/{}_results/result_{}_{}.json'.format(args.setting, args.prompt_type, args.num)
  else:
    file_txt = '../results/chatgpt_results/{}_results/result_{}_{}.json'.format(args.setting, args.prompt_type, args.num)
  with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)
  print('save path', file_txt)


