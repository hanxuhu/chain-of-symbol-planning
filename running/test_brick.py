import os
from time import sleep
import openai
import json
openai.api_key = "xxx" #"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"#os.getenv("OPENAI_API_KEY")
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

args = parser.parse_args()


import json

prompt_type = args.prompt_type
setting = args.setting
if args.setting == 'noshuffle':
   setting = 'shuffle_descpt'
prompt = open('demo/{}_demo_{}_2.txt'.format(prompt_type,args.setting)).read()
#cot_prompt_1d = open('demo/davinci_cos_1d.txt').read()
#base_prompt = open('demo/baseline_demo.txt').read()
model_name = args.model_name
# Opening JSON file
f = open('data_brick_{}_5shot_cos_1_drop.json'.format(args.setting))
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
    file_txt = 'chatgpt_results/cos_noshuffle_results_drop.json'
    with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)
else:
   file_txt = 'chatgpt_results/brick_{}_5shot_{}_{}_drop.json'.format(args.setting, prompt_type, args.num)
   with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)
'''

f = open('data_brick_shufflelabel.json')
zeroshot_prompt = 'Lets think step by step, and provide the answer in the format of a sequence of bricks by a comma in the last sentence.'
data = json.load(f)
res_list = []
res_label = []
constraint_prompt = 'You only need to return the sequence of removed bricks in order from top to bottom, without any explaination. So the answer is:'
cos_1d_desc = "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n" #+Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"},
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
    file_txt = 'davinci003_results/brick_1d_cot_results/shuffle_both/results.json'
    with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)
else:
   file_txt = 'chatgpt_results/brick_shufflelabel_5shot_cot.json'.format(prompt_type)
   with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)


f = open('data_brick_noshuffle.json')
zeroshot_prompt = 'Lets think step by step, and provide the answer in the format of a sequence of bricks by a comma in the last sentence.'
data = json.load(f)
res_list = []
res_label = []
constraint_prompt = 'You only need to return the sequence of removed bricks in order from top to bottom, without any explaination. So the answer is:'
cos_1d_desc = "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n" #+Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"},
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
    file_txt = 'davinci003_results/brick_1d_cot_results/shuffle_both/results.json'
    with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)
else:
   file_txt = 'chatgpt_results/brick_noshuffle_5shot_cot.json'.format(prompt_type)
   with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)
   


res_list = []
res_label = []
for item in data:
  prompt = cos_prompt+'\nStory and Question:'+item['data']+'\n'
  i+=1
  print(i)
  #print(prompt)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
  )
  res = response['choices'][0]['message']['content']
  #print(res[-100:])
  #print(item['label'])
  dict_res = {'pred':res, 'label': item['label']}
  #res_label.append(item['label'])
  res_list.append(dict_res)
  #sleep(15)
#res_final = {res_list}

with open('cos_prompt_results/shuffle_both_result.json', 'w') as outfile:
        json.dump(res_list, outfile)

'''
'''
res_list = []
res_label = []
for item in data[200:300]:
  i+=1
  print(i)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=600,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": item['data']},
    ]
  )
  res = response['choices'][0]['message']['content']
  dict_res = {'pred':res, 'label': item['label']}
  #res_label.append(item['label'])
  res_list.append(dict_res)
  sleep(15)
#res_final = {res_list}
with open('shuffle_both_result3.json', 'w') as outfile:
        json.dump(res_list, outfile)


f = open('brick_2d/shuffle_label_2d.json')
data = json.load(f)

i=0
res_list = []
res_label = []
for item in data:
  prompt = cos_prompt_2d + '\n\n' + 'Question:' + '\n\n' + item['data'] + '\n\n' + "Using the symbolic method to convert text to symbols, B->A means A is in front of B and C->B means B is in front of C and C//D means D is on top of C. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):"#+ "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"
  i+=1
  print(i)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
  )
  res = response['choices'][0]['message']['content']
  print(res[-100:])
  print(item['label'])
  dict_res = {'pred':res, 'label': item['label']}
  #res_label.append(item['label'])
  res_list.append(dict_res)
  #sleep(15)
#res_final = {res_list}
with open('cos_prompt_results/shuffle_label_result_2d.json', 'w') as outfile:
        json.dump(res_list, outfile)


f = open('brick_2d/shuffleboth_brick_2d.json')
data = json.load(f)
i = 0
res_list = []
res_label = []
for item in data:
  prompt = cot_prompt + '\n\n' + 'Question:' + '\n\n' + item['data'] + '\n\n' #+ "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"
  i+=1
  print(i)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
  )
  res = response['choices'][0]['message']['content']
  dict_res = {'pred':res, 'label': item['label']}
  #res_label.append(item['label'])
  res_list.append(dict_res)
  sleep(3)
#res_final = {res_list}
with open('cot_prompt_results/shuffleboth_result_2d.json', 'w') as outfile:
        json.dump(res_list, outfile)





f = open('brick_2d/shuffle_descrpt_2d.json')
data = json.load(f)

i = 0
res_list = []
res_label = []
for item in data:
  prompt = cos_prompt_2d + '\n\n' + 'Question:' + '\n\n' + item['data'] + '\n\n' + "Using the symbolic method to convert text to symbols, B->A means A is in front of B and C->B means B is in front of C and C//D means D is on top of C. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):"#"Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"
  i+=1
  print(i)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
  )
  res = response['choices'][0]['message']['content']
  dict_res = {'pred':res, 'label': item['label']}
  #res_label.append(item['label'])
  res_list.append(dict_res)
  sleep(3)
#res_final = {res_list}
with open('cos_prompt_results/shuffle_descrpt_result_2d.json', 'w') as outfile:
        json.dump(res_list, outfile)


f = open('brick_2d/shuffle_descrpt_2d.json')
data = json.load(f)
i = 0

res_list = []
res_label = []

while True:
    item = data[i]
    try:
        prompt = cot_prompt + '\n\n' + 'Question:' + '\n\n' + item['data'] + '\n\n' #+ "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"
        
        print(i)
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          max_tokens=2048,
          temperature=0,
          messages=[
             {"role": "system", "content": "You are a helpful assistant."},
             {"role": "user", "content": prompt},
          ]
        )
        res = response['choices'][0]['message']['content']
        dict_res = {'pred':res, 'label': item['label']}
        #res_label.append(item['label'])
        res_list.append(dict_res)
        i+=1
    except i==499:
        break
    except:
        print("error")



#i = 0
#res_list = []
#res_label = []
for item in data[100:]:
  prompt = cot_prompt + '\n\n' + 'Question:' + '\n\n' + item['data'] + '\n\n' #+ "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"
  i+=1
  print(i)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
  )
  res = response['choices'][0]['message']['content']
  dict_res = {'pred':res, 'label': item['label']}
  #res_label.append(item['label'])
  res_list.append(dict_res)
  sleep(10)
#res_final = {res_list}

with open('cos_prompt_results/shuffle_descrpt_result_2d.json', 'w') as outfile:
        json.dump(res_list, outfile)


i=0

f = open('brick_2d/shuffleboth_brick_2d.json')
data = json.load(f)


res_list = []
res_label = []
for item in data:
  prompt = cos_prompt_2d + '\n\n' + 'Question:' + '\n\n' + item['data'] + '\n\n' + "Using the symbolic method to convert text to symbols, B->A means A is in front of B and C->B means B is in front of C and C//D means D is on top of C. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):"#"Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"
  i+=1
  print(i)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
  )
  res = response['choices'][0]['message']['content']
  dict_res = {'pred':res, 'label': item['label']}
  #res_label.append(item['label'])
  res_list.append(dict_res)
  sleep(10)
#res_final = {res_list}
with open('cos_prompt_results/shuffleboth_result_2d.json', 'w') as outfile:
        json.dump(res_list, outfile)





res_list = []
res_label = []
for item in data:
  prompt = cot_prompt + '\n\n' + 'Question:' + '\n\n' + item['data'] + '\n\n' #+ "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"
  i+=1
  print(i)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
  )
  res = response['choices'][0]['message']['content']
  dict_res = {'pred':res, 'label': item['label']}
  #res_label.append(item['label'])
  res_list.append(dict_res)
  sleep(10)
#res_final = {res_list}
with open('cot_prompt_results/no_shuffle_result_2d.json', 'w') as outfile:
        json.dump(res_list, outfile)
'''





