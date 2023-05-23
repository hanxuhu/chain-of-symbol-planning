import json
#f_cos = open('cos_prompt_results/shuffle_both_result_cos.json')
#f_cot = open('cot_prompt_results/shuffle_descp_result.json')
data_final = []
for i in range(1):
   f_path ='chatgpt_results/navigation_results/result_zeroshot.json'.format(i)
   f_cos = open(f_path)
   data_cos = json.load(f_cos)
   data_final += data_cos
#data_cot= json.load(f_cot)
#data = data['']
import re


def parse(text):

    #string = "This is a string to remove brick and find the first letter after it. We also need to remove brick again."
    bricks = re.findall(r"[A-J]", text)
    brick_names = []
    i = 0
    #print(bricks)
    '''
    for brick in bricks:
        if brick ==bricks[0]:
            print(1)
            brick_names.append(brick[0])
        elif brick ==bricks[-1]:
            brick_names.append(brick[1])
            brick_names.append(brick[2])
        else:
            brick_names.append(brick[1])
            
    '''
    '''
    x = ''
    for item in bricks:
        x+=item
    result = re.sub(r'(\w+)\1+', r'\1', x)
    '''
    result = ''
    pattern = "the answer is ([A-Z, ]+)"  #r"result as ([A-Z, ]+)" for brick
    
    match = re.search(pattern, text)
    if match:
      result = match.group(1).replace(", ", "")
      #print(result)
    return result

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
p, r = 0, 0
ac = 0
for item in data_final:
    pred = item['pred']
    #print(i)
    text = str(pred[-200:])
    #print(text)
    

    text_list = text.split("sequence")
    #print(text_list)
    uppercase_letters = ""
    for char in text_list[-1]:
      if char.isupper():
         uppercase_letters += char
    if uppercase_letters[0] == uppercase_letters[1]:
       uppercase_letters = uppercase_letters[1:]
    print(uppercase_letters)
    print(item['label'])
    res = uppercase_letters
    if res == item['label']: #or res == item['label'][:-1]: #or res[:-1]==item['label']:
       ac += 1
    lcs = longest_common_substring(res,item['label'] )
    r += len(lcs)/len(item['label'])
    if len(res)==0:
        continue
    p += len(lcs)/len(res)
    i += 1
    #ac = 0

acc = ac/i
print('acc', acc)
print(p/i)
print(r/i)
