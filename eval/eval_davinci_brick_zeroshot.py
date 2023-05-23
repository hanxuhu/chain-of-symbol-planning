import json
#f_cos = open('cos_prompt_results/shuffle_both_result_cos.json')
#f_cot = open('cot_prompt_results/shuffle_descp_result.json')
data_final = []
for i in range(1):
   f_path = 'chatgpt_results/brick2d_shuffle_both_zeroshot.json'.format(i) #'davinci003_results/navigation_results/result50_100.1.json'.format(i)
   f_cos = open(f_path) #encoding="utf-8"
   data_cos= json.load(f_cos)
   data_final += data_cos
#data_cot= json.load(f_cot)
#data = data['']
import re


def parse(text):
    print('text',text)

    #string = "This is a string to remove brick and find the first letter after it. We also need to remove brick again."
 
    pattern = r".*?([A-Z]+)" #r"remove.*?([A-Z]+)" #"the answer is ([A-Z, ]+)."  #
    
    matches = re.findall(pattern, text)
    return matches

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
def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]

i = 1
ac = 0
p,r =0 ,0 
for item in data_final:
    text = item['pred']#"To get brick B, first remove the yellow brick A from the top of the brick C. Then remove the yellow brick C from the top of the brick B. Finally, grab the brick B."
    print(text)
    res = parse(text)
    text_list = text.split('\n')#text.split("equence")
    
    uppercase_letters = ""
    target_sentence = text_list[-1] if text_list[-1] != '' else text_list[-2]
    for char in target_sentence:
       if char.isupper():
           uppercase_letters += char
    if len(uppercase_letters)>1:
      if uppercase_letters[0] in uppercase_letters[1:]:
         res_str = uppercase_letters[1:]
      else:
         res_str = uppercase_letters
    else:
        res_str = uppercase_letters
   
     
    
    uppercase_letters = uppercase_letters[1:]
    if uppercase_letters[0] == uppercase_letters[-1]:
           uppercase_letters = uppercase_letters[1:]
    res_str = uppercase_letters
   
    #res = parse(text)
    #res  = res_str
    
    #res = res.replace("T", "")
    #res = res.replace("F", "")
    res_str = ''
    for char in res:
        res_str+=char
    res = res_str
    print('res', res)
    print('label',item['label'])
    i += 1
    if item['label']=='we dont need to remove':
       if len(res)==1 or len(res)==0:
          ac +=1
          p+=1
          r+=1
     
       continue
    elif res == item['label'] or res == item['label'][:-1] or res[:-1]==item['label']:
       ac += 1
    lcs = longest_common_substring(res,item['label'] )
    r += len(lcs)/len(item['label'])
    if len(res)==0:
        continue
    p += len(lcs)/len(res)
    '''
    #print(res_str)
    print('label', item['label'])
    if item['label']=='we dont need to remove':
       if len(res_str)==0 or len(res_str)==1:
          ac +=1
    elif res_str == item['label'] or res_str == item['label'][:-1]: #or res[:-1]==item['label']:
       ac += 1
       #print('ac')
    i += 1
    print(i)
    '''
print(ac)
acc = ac/(i-1)
recall = r/(i-1)
precision = p/(i-1)
print('acc', acc)
print('precision', precision)
print('recall', recall)
'''
for item in data_final:
    pred = item['pred']
    #print(i)
    text = str(pred[-200:])
    #print(text)
    


    res = parse(pred[-100:])
    #print('a',pred[-100:])
    #print(pred)
    #print('res',res)
    #print('label',item['label'])
    if item['label']=='we dont need to remove':
       if len(res)==1:
          ac +=1
    elif res == item['label']: #or res == item['label'][:-1] or res[:-1]==item['label']:
       ac += 1
    i += 1
print(i)
acc = ac/i
print('acc', acc)
'''