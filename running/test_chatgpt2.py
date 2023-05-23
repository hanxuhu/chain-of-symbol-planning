import os
from time import sleep
import openai
import json
openai.api_key = "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"#os.getenv("OPENAI_API_KEY")

def process(response):
  print(response)
  json_object = json.dumps(response["choices"][0]["message"]["content"], ensure_ascii=False).encode('utf8')
  print(json_object.decode())
  return json_object.decode()



import json
  
# Opening JSON file
f = open('data_brick_noshuffle.json')
data = json.load(f)
res_list = []
res_label = []
cos_prompt = open('./COS_demo.txt').read()
constraint_prompt = 'You only need to return the sequence of removed bricks in order from top to bottom, without any explaination. So the answer is:'
i = 0
'''
for item in data[100:200]:
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
with open('shuffle_both_result1.json', 'w') as outfile:
        json.dump(res_list, outfile)
'''
res_list = []
res_label = []
for item in data:
  prompt = cos_prompt+'\nStory and Question:'+item['data']+'\n'
  print(prompt)
  i+=1
  print(i)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=600,
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
  sleep(15)
#res_final = {res_list}

with open('noshuffle_result.json', 'w') as outfile:
        json.dump(res_list, outfile)



'''
#print(response)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="non",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#print(response)
'''



