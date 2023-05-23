import os
from time import sleep
import openai
import json
openai.api_key = "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" #"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"#os.getenv("OPENAI_API_KEY")

def process(response):
  print(response)
  json_object = json.dumps(response["choices"][0]["message"]["content"], ensure_ascii=False).encode('utf8')
  print(json_object.decode())
  return json_object.decode()



import json
#cot_prompt = open('demo/cot_demo_1.txt').read()
cos_prompt_1d = open('demo/nlvr_cos.txt').read()
base_prompt = open('demo/baseline_demo.txt').read()
  
# Opening JSON file

f = open('data_brick_shuffle_both.json')

data = json.load(f)
res_list = []
res_label = []
constraint_prompt = 'You only need to return the sequence of removed bricks in order from top to bottom, without any explaination. So the answer is:'
cos_1d_desc = "Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n" #+Using the symbolic method to convert text to symbols, B//A means A is on top of B. Then combine the relation together, then solve this question recursively and keep the last sentence as the format of 'so we get the result as (the sequence of names of bricks in order):\n\n"},
i = 0
step = 0
for i in range(10):
  res_list = []
  for item in data[i*50: (i+1)*50]:
   step +=1
   print(step)
   response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": cos_prompt_1d  + '\n' +  'Question:' + '\n' +  item['data'] + '\n'+"Answer:"
        }
    ]
   )
   res = response['choices'][0]['message']['content']
   dict_res = {'pred':res, 'label': item['label']}
   #res_label.append(item['label'])
   res_list.append(dict_res)
   print(dict_res)
   sleep(3)
   #res_final = {res_list}
  file_txt = 'cos_2_1d_results/shuffle_both/result{}.json'.format(i)
  with open(file_txt, 'w') as outfile:
        json.dump(res_list, outfile)

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





