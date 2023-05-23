import json
#f_cos = open('cos_prompt_results/shuffle_both_result_cos.json')
#f_cot = open('cot_prompt_results/shuffle_descp_result.json')
import re
import math

def compute(a,b, c):
  mean = (a + b + c) / 3

  da = a - mean
  db = b - mean
  dc = c - mean

  s = da**2 + db**2 + dc**2

  std_dev = math.sqrt(s/3)

  print('standard error',std_dev)
  print('average', mean)

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
def eval(f_path):
  data_final = []
  #for i in range(1):
  #f_path ='davinci003_results/navigation_results/result_cos_2.json'.format(i)
  f_cos = open(f_path)
  data_cos = json.load(f_cos)
  data_final += data_cos
  #data_cot= json.load(f_cot)
  #data = data['']
  i = 1
  ac = 0
  p, r = 0,0
  for item in data_final:
    res = item['pred']
    if res[-1] == '.':
       res = res[:-1]
    #print(i)
    #print(text)
    res_parsed = parse(res)
    
    #print('a',pred[-100:])
    #print(pred)
    #print('res',res_parsed)
    #print('label',item['label'])
    if item['label']=='we dont need to remove':
       if len(res)==0:
          ac +=1
    elif res_parsed == item['label']: #or res == item['label'][:-1] or res[:-1]==item['label']:
       ac += 1
    label = item['label']
    lcs = longest_common_substring(res_parsed,label )
    if len(label) > 1:
      r += len(lcs)/len(label)
    else:
       if len(label) == 0:
          r +=1
       else:
          r+=0
    if len(res_parsed)==0:
        continue
    p += len(lcs)/len(res_parsed)
    i += 1
  acc = ac/i
  pre = p/i
  rec = r/i
  print('acc', acc)
  print('pre', pre)
  print('rec', rec)
  return acc, pre, rec



ac1, p1, r1 = eval('../results/davinci003_results/navigation_results/result_cos_2.json')
ac2, p2, r2 = eval('../results/davinci003_results/navigation_results/result_cos_3.json')
ac3, p3, r3 = 0.75, 0.883, 0.901
print("\n\nfor cos davinci")
print('acc')
compute(ac1, ac2, ac3)
print('pre')
compute(p1, p2, p3)
print('rec')
compute(r1, r2, r3)

ac1, p1, r1 = eval('../results/davinci003_results/navigation_results/result_cot_2.json')
ac2, p2, r2 = eval('../results/davinci003_results/navigation_results/result_cot_3.json')
ac3, p3, r3 = 0.687, 0.862, 0.867 
print("\n\nfor cot davinci")
print('acc')
compute(ac1, ac2, ac3)
print('pre')
compute(p1, p2, p3)
print('rec')
compute(r1, r2, r3)

print("\n\nfor cos chatgpt")
#compute chatgpt results cos
print('acc')
compute(67.4,58.7,66.1) #acc
print('pre')
compute(82.9,79.9,82.4) #pre
print('rec')
compute(85.3,83.6,84.5) #rec

print("\n\nfor cot chatgpt")
#compute chatgpt results cot
print('acc')
compute(54.9,49.8,56.2) #acc
print('pre')
compute(76.2,75.0,77.7) #pre
print('rec')
compute(82.0,80.6,82.6) #rec

'''
i = 1
ac = 0
for item in data_final:
    pred = item['pred']
    #print(i)
    text = str(pred[-200:])
    #print(text)
    

    text_list = text.split("Therefore")
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
      ac += 1
      print(1)
    i += 1
    #ac = 0

acc = ac/i
print('acc', acc)
'''