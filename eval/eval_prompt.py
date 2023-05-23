import json
#f_cos = open('cos_prompt_results/shuffle_both_result_cos.json')
#f_cot = open('cot_prompt_results/shuffle_descp_result.json')
import argparse
parser = argparse.ArgumentParser(description="eval LLM planning abilities")
parser.add_argument(
        "--prompt_type",
        type=str,
        default='cos',
        help="type of prompt",
    )

parser.add_argument(
        "--setting",
        type=str,
        default='shuffle_both',
        help="setting",
    )

parser.add_argument(
        "--num",
        type=str,
        default='1',
        help="num",
    )

args = parser.parse_args()
data_final = []

f_path = '../results/chatgpt_results/brick_{}_5shot_{}_{}.json'.format(args.setting, args.prompt_type, args.num)  #brick_{}_5shot_{}_{}.json'.format(args.setting, args.prompt_type, args.num) #'chatgpt_results/brick_{}_5shot_{}_{}_drop.json'.format(args.setting, args.prompt_type, args.num) #'davinci003_results/navigation_results/result50_100.1.json'.format(i)
f_cos = open(f_path)
data_cos= json.load(f_cos)
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
    pattern = r"result as ([A-Z, ]+)"  #"the answer is ([A-Z, ]+)."  #
    
    match = re.search(pattern, text)
    #print(match)
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
#print(len(data_final))
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
 # 

def compute_res(data_final):
  i = 1
  r = 0
  p = 0
  ac = 0
  #  recall = 0
  correct_id = []
  wrong_id = []
  for item in data_final:
    pred = item['pred']
    #print(i)
    #print(pred[-200:])
    text = str(pred[-200:])
    #print(text)
    

    #print(pred[-100:])
    res = parse(pred[-100:])
    res = str(res)
    #print('res', res)
    #print('label', str(item['label']))
    label = str(item['label'])
    #print('a',pred[-100:])
    #print(pred)
    #print('res',res)
    #print('label',item['label'])
    i += 1
    if label =='we dont need to remove':
       if len(res)==1 or len(res)==0:
          correct_id.append(i-1)
          ac +=1
          p+=1
          r+=1
     
       continue
    elif res == label or res == label[:-1]: #or res[:-1]==item['label']:
       ac += 1
       correct_id.append(i-1)
    lcs = longest_common_substring(res,label )
    r += len(lcs)/len(label)
    if len(res)==0:
        continue
    p += len(lcs)/len(res)
    if i-1 not in correct_id:
       wrong_id.append(i-1)
   
  acc = float(ac)/(i-1)

  recall = float(r)/(i-1)
  precision = float(p)/(i-1)
  print('acc', acc)  
  print('precision', precision)
  print('recall', recall)
  res = f_path + ' acc:' + str(acc) + ', precision:' +str(precision) + ', recall:' + str(recall) + '\n'
  '''
  file = open("results_for_eval.txt", "a")
  file.write(res)
  file.close()
  '''
  return correct_id, wrong_id

correct_id, wrond_id = compute_res(data_final)

# data_final_1 = []
# for i in range(1):
#    f_path = 'chatgpt_results/brick_shuffle_descpt_5shot_cot_2_drop.json' #brick_{}_5shot_{}_{}.json'.format(args.setting, args.prompt_type, args.num) #'chatgpt_results/brick_{}_5shot_{}_{}_drop.json'.format(args.setting, args.prompt_type, args.num) #'davinci003_results/navigation_results/result50_100.1.json'.format(i)
#    f_cos = open(f_path)
#    data_cos= json.load(f_cos)
#    data_final_1 += data_cos

# correct_id, _ = compute_res(data_final)
# _, wrond_id = compute_res(data_final_1)
# set1 = set(correct_id)
# set2 = set(wrond_id)
# print(set1)
# print(set2)
# #print(data_final)
# common_set = set1 & set2 
# print(common_set)
'''
i = 1
ac = 0
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
