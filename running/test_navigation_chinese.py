import os
from time import sleep
import openai
import json
openai.api_key ="xxxx"#os.getenv("OPENAI_API_KEY")

def process(response):
  print(response)
  json_object = json.dumps(response["choices"][0]["message"]["content"], ensure_ascii=False).encode('utf8')
  print(json_object.decode())
  return json_object.decode()



import json
#cot_prompt = open('demo/cot_demo_1.txt').read()
cos_prompt = open('../demo/navigation_cos_chinese.txt').read()
cot_prompt = open('../demo/navigation_cot_chinese.txt').read()
zero_shot_prompt = "Let's think step by step, and provide the answer as the format of sequence of landmarks seperated by comma in the last sentence."
model_name = 'chatgpt'
# Opening JSON file

f = open('chinese_data/navigation.json')

data = json.load(f)
res_list = []
res_label = []
constraint_prompt = 'You only need to return the sequence of removed bricks in order from top to bottom, without any explaination. So the answer is:'
cos_1d_desc = "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n" #+Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"},
i = 0
step = 0
for i in range(1):
  if i == 1:
      cos_prompt = cot_prompt 
  #res_list = []
  for item in data[80:]:
   #print(item['Story'])
   step +=1
   res_list = []
   if step%10==0:
    print(step)
   #print(step)
   res = ''
   while 1:
      
      try:
        if model_name == 'text-davinci-003':
           response = openai.Completion.create(
            model=model_name,
            prompt= '故事：' + item['Story'] + '\n' + '问题：' + item['Question'] + '\n' + '答案：\n',#cos_prompt_1d  + '\n' +  'Story:' + '\n' +  item['story'] + '\n'+"Question:" +  '\n'+ item['question'] + '?',
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
            {"role": "user", "content": cos_prompt + '\n\n' + item['data']  + '\n'  ,  #cos_prompt + '\n\n' + item['Story'] +  '\n'+ item['Question']
            }]
          )
           if model_name == 'text-davinci-003':
             res = response['choices'][0]['text']
           else:
             res = response['choices'][0]['message']['content']
        break
      except:
        res_list.append('error')
        print("error")
        sleep(5)
        print(len(res_list))
        if len(res_list)>3:
           print(step)
           break
        #break
   
   if res == '':
      continue
   dict_res = {'pred':res, 'label': item['label']}
   #res_label.append(item['label'])
   res_list.append(dict_res)
   #print(dict_res)
   #sleep(3)
   #res_final = {res_list}
  file_txt = 'chatgpt_results/navigation_results/result_chinese_cos.json' #.format(i)
  with open(file_txt, 'w', encoding="utf-8") as outfile:
        json.dump(res_list, outfile, ensure_ascii=False)

