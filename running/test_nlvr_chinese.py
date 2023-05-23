import os
from time import sleep
import openai
import json
openai.api_key ="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"#os.getenv("OPENAI_API_KEY")

def process(response):
  print(response)
  json_object = json.dumps(response["choices"][0]["message"]["content"], ensure_ascii=False).encode('utf8')
  print(json_object.decode())
  return json_object.decode()



import json
#cot_prompt = open('demo/cot_demo_1.txt').read()
cos_prompt = open('demo/nlvr_cos_chinese.txt').read()
base_prompt = open('demo/baseline_demo.txt').read()
model_name = 'gpt-3.5-turbo'
# Opening JSON file
prompt_zeroshot = "Let's think step by step, and provide the answer as the format of sequence of the objects needed to move seperated by comma in the last sentence."
f = open('chinese_data/nlvr.json')

data = json.load(f)
res_list = []
res_label = []
constraint_prompt = 'You only need to return the sequence of removed bricks in order from top to bottom, without any explaination. So the answer is:'
cos_1d_desc = "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n" #+Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"},
i = 0
step = 0
for i in range(1):
  res_list = []
  for item in data:
   while 1:
      try:
          step +=1
          if step%10==0:
            print(step)
          if model_name == 'text-davinci-003': 
            response = openai.Completion.create(
             model= model_name,
             prompt= item['data'] + '\n'+ item['question'] + '?' + '\n' + prompt_zeroshot, #prompt_zeroshot + '\n\n' +'Story:' + '\n' +  item['story'] + '\n'+"Question:" +  '\n'+ item['question'] + '?' ,#cos_prompt_1d  + '\n' +  'Story:' + '\n' +  item['story'] + '\n'+"Question:" +  '\n'+ item['question'] + '?',
             temperature=0,
             max_tokens=2048,
             top_p=1,
             frequency_penalty=0,
             presence_penalty=0
            )
          else:
            response = openai.ChatCompletion.create(
                model=model_name,
                temperature=0,
                messages=[
                 {"role": "system", "content": "You are a helpful assistant."},
                 {"role": "user", "content": cos_prompt + '\n\n' + '问题：' + item['data']  + '\n' + '答案：\n', #cos_prompt_1d  + '\n' +  'Story:' + '\n' +  item['story'] + '\n'+"Question:" +  '\n'+ item['question'] + '?'
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
          break
   '''
   response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": 'Story:' + '\n' +  item['story'] + '\n'+"Question:" +  '\n'+ item['question'] + '?'#cos_prompt_1d  + '\n' +  'Story:' + '\n' +  item['story'] + '\n'+"Question:" +  '\n'+ item['question'] + '?'
        }
    ]
   )
   '''
   
   #print(dict_res)
   #sleep(3)
   #res_final = {res_list}
  if model_name == 'gpt-3.5-turbo':
      model_name = 'chatgpt'
  else:
      model_name= 'davinci003'
  file_txt = '{}_results/nlvr_results/result_chinese.json'.format(model_name)
  with open(file_txt, 'w', encoding="utf-8") as outfile:
        json.dump(res_list, outfile,  ensure_ascii=False)

'''
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

'''



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
'''

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
'''

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

'''



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





