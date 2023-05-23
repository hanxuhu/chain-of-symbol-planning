import json
#f_cos = open('cos_prompt_results/shuffle_both_result_cos.json')
#f_cot = open('cot_prompt_results/shuffle_descp_result.json')
data_final = []

f_path ='../results/chatgpt_results/nlvr_results/result_zeroshot.json'
f_cos = open(f_path)
data_final = json.load(f_cos)

#data_cot= json.load(f_cot)
#data = data['']
import re

'''
i = 1
ac = 0
for item in data_final:
    res = item['pred']
    if res[-1] == '.':
       res = res[:-1]
    print(i)
    #print(text)
    
    #print('a',pred[-100:])
    #print(pred)
    print('res',res)
    print('label',item['label'])
    if item['label']=='we dont need to remove':
       if len(res)==1:
          ac +=1
    elif res == item['label']: #or res == item['label'][:-1] or res[:-1]==item['label']:
       ac += 1
    i += 1
acc = ac/i
print('acc', acc)


'''
print(data_final[0])
step = 0
ac = 0
r, p = 0,0 
for item in data_final:
    pred = item['pred']
    #print(step)
    text = str(pred[-200:])
    #print(text)
    label = item['label']
    for i in range(len(label)):
       label[i] = set(label[i][1:])
    #label = set(label)
    text_last = text.split("\n")[-1]
    text_proc = text_last.split(',')
    
    for i in range(len(text_proc)):
       #print(text_proc[i].split())
       text_proc[i] = set(text_proc[i].split())
    #print('label', label)
    label_need_remove = []
    label_length = len(label)
    for label_item in label:
        #print('label item', label_item)
        for item in text_proc:
          #print('item', item)
          if label_item.issubset(item):
             #print(111)
             label_need_remove.append(label_item)
    if label_length == 0:
       if len(label_need_remove) == 0:
          r+=1
    else:
       r += len(label_need_remove) / label_length
    if len(text_proc)>1:
       p += len(label_need_remove) / (len(text_proc)-1)
    else: 
       p+=0
    for item in label_need_remove:
       if item in label:
          label.remove(item)
    
    #print(label)
    if label == []:
       ac += 1
       #print(step)
    '''             
    #print(text_list)
    uppercase_letters = ""
    for char in text_list[-1]:
      if char.isupper():
         uppercase_letters += char
    if uppercase_letters[0] == uppercase_letters[1]:
       uppercase_letters = uppercase_letters[1:]
    print(uppercase_letters)
    print(item['label'])
    if uppercase_letters == item['label']:
    '''
    
    step += 1.0
    #ac = 0
print(ac)
print(step)
acc = ac/step
recall = r/step
precision = p/step
print('acc', acc)
print('recall', recall)
print('precision', precision)
