import json
import re
#f_cos = open('cos_prompt_results/shuffle_both_result_cos.json')
#f_cot = open('cot_prompt_results/shuffle_descp_result.json')

def eval(f_path):
  data_final = []
  step = 0
  index_cos = []

  #for i in range(1):
    #f_path = 'chatgpt_results/nlvr_results/result_cos_3.json'.format(i)
  f_cos = open(f_path)
  data_cos= json.load(f_cos)
  data_final += data_cos
  ac = 0
  p = 0
  r = 0
  for data in data_final:
   step+=1
   res = data['label']
   #print(res)
   res_new = []
   for item in res:
      x = item[0]
      item[0] = item[2]
      item[2] = x
   res_new = []
   for item in res:
      res_new.append(item)
   res = res_new
   res_str = set()
   #print(res)
   for item in res:
     res_str.add(str(item))
   #print('res_str', res_str)
   #pattern = r"\(([^,]+),\s*([^,]+),\s*([^)]+)\)\s+(left|middle|right)"
   #matches = re.findall(pattern,data['pred'])
   #spattern = r'\((black|white|yellow|blue),\s(triangle|square|round),\s(small|large|middle),\s(middle|right|left)\)'
   pattern = r'\((small|large|middle),\s(triangle|square|round),\s(black|white|yellow|blue)\) (right|middle|left)'
   #print(data['pred'][-200:])
   matches = re.findall(pattern, data['pred'])
   #print(data['pred'])
   matches = [str(list(match)) for match in matches]
   
   #print('matches',matches)

   pred_set = set(matches)
   #print('pred_set', pred_set)
   #print('res_str', res_str)
   #print(res_str)
   if len(res_str) == 0 or len(pred_set) == 0 :
     if len(pred_set)==0 and len(res_str) == 0 :
        ac+=1
        p+=1
        r+=1
     else:
        ac+=0
        p+=0
        r+=0
   else:
     overlap_count = len(pred_set & res_str)
     #print('overlap_count', overlap_count)
     #print('res_set', len(res_str))
     if res_str.issubset(pred_set):#overlap_count == len(res_str) == len(pred_set):
        ac+=1
     else:
        index_cos.append(step)
     p += float(overlap_count/ (len(pred_set)))
     r += float(overlap_count/ (len(res_str)))
  ac = float(ac)
  p_all = p/len(data_final)
  r_all = r/len(data_final)
  ac_all = ac/len(data_final)
  print('precision', p_all)
  print('recall', r_all)
  print('acc', ac_all)

  return ac_all, p_all, r_all



import math


def compute(a,b, c):
  mean = (a + b + c) / 3
  da = a - mean
  db = b - mean
  dc = c - mean
  s = da**2 + db**2 + dc**2
  std_dev = math.sqrt(s/3)

  print("the standard error of these three numbers:", std_dev)
  print('average', mean)
ac1, p1, r1 = eval('../results/davinci003_results/nlvr_results/result_cos_2.json')
ac2, p2, r2 = eval('../results/davinci003_results/nlvr_results/result_cos_3.json')
ac3, p3, r3 = 0.717, 0.864, 0.827 #0.655, 0.701, 0.802
compute(ac1, ac2, ac3)
compute(p1, p2, p3)
compute(r1, r2, r3)

def eval_cot(f_path):
  data_final = []
  index_cot = []
  step = 0
  for i in range(1):
   #f_path = 'chatgpt_results/nlvr_results/result_cot_3.json'.format(i)
   f_cot = open(f_path)
   data_cot= json.load(f_cot)
   data_final += data_cot

  # Define a dictionary to map words to their desired order and format
  word_map = {
    "move": None,
    "": None,
    "the": None,
    "small": "small",
    "large": "large",
    "middle": "middle",
    "triangle": "triangle",
    "triangles": "triangle",
    "the": None,
    "one": None,
    "of":None,
    "other": None,
    "another": None,
    "round": "round",
    "rounds": "round",
    "square": "square",
    "squares": "square",
    "in": None,
    "black": "black",
    "yellow": "yellow",
    "blue": "blue",
    "white": "white",
    "from": None,
    "the": None,
    "left": "left",
    "box": None,
    "to": None,
    "the": None,
    "right": "right",
    "circles": None,
    "two": None,
    "all": None,
    "and": None,
    "box": None
  }
  ac = 0
  p = 0
  r = 0
  step = 0
  for item in data_final:
    step +=1
    text = item['pred']
    sentences = text.split('\n')
    moves = []
    for sentence in sentences:
      if 'Move' in sentence:
        moves.append(sentence[2:])
    pred_parsed_list = []
    new_moves = []
    pred_other = []
    for sentence in moves:
       if ('right box to the right box' not in sentence) and ('left box to the left box' not in sentence) and ('middle box to the middle box' not in sentence):
          new_moves.append(sentence)
       else:
          pred_other.append(new_moves)
    moves = new_moves
    #print(moves)
    #print(moves) # Output: ['1. Move the small triangle in black from the middle box to the right box.', '2. Move the small square in black from the middle box to the right box.', '3. Move the large round in black from the middle box to the right box.']
    for sentence in moves:
        #Split the sentence into words
        words = sentence.split()
        if len(words)!=14:
           continue
        # Remove any punctuation or capitalization from the words
        words = [w.lower().strip(",.") for w in words]
        # Map each word to its desired format using the dictionary
        for w in words:
           if w not in word_map.keys():
              word_map[w] = None
        formatted_words = [word_map[w] for w in words]
        # Remove any None values from the formatted words
        formatted_words = [w for w in formatted_words if w is not None]
        formatted_words.pop()
        x = formatted_words[0]
        formatted_words[0] = formatted_words[2]
        formatted_words[2] = x
        #print(x)
        # Print the final list of formatted words
        #print(formatted_words)
        pred_parsed_list.append(str(formatted_words))
    pred_set = set(pred_parsed_list)
    #print(pred_set)
    res = item['label']
    res_str = set()
    #print(res)
    for item in res:
      res_str.add(str(item))
    if len(res_str) == 0 or len(pred_set) == 0 :
     if len(pred_set)==0 and len(res_str) == 0 :
        ac+=1
        p+=1
        r+=1
     else:
        ac+=0
        p+=0
        r+=0
    else:
     overlap_count = len(pred_set & res_str)
     #print('overlap_count', overlap_count)
     #print('res_set', len(res_str))

     #if overlap_count == len(res_str):
     #   ac+=1
     if res_str.issubset(pred_set):#overlap_count == len(res_str) == len(pred_set):
        ac+=1
     else:
        index_cot.append(step)
     p += float(overlap_count/ (len(pred_set) + len(pred_other)))
     r += float(overlap_count/ (len(res_str)))
     ac = float(ac)
  p_all = p/len(data_final)
  r_all = r/len(data_final)
  ac_all = ac/len(data_final)
  print('precision', p_all)
  print('recall', r_all)
  print('acc', ac_all)
  print(len(data_final))
  #print(index_cos)
  #print(index_cot)
  return ac_all, p_all, r_all

ac1, p1, r1 = eval_cot('../results/davinci003_results/nlvr_results/result_cot_2.json')
ac2, p2, r2 = eval_cot('../results/davinci003_results/nlvr_results/result_cot_3.json')
ac3, p3, r3 = 0.67, 0.7, 0.802  #0.615, 0.661, 0.791 for chatgpt
compute(ac1, ac2, ac3)
compute(p1, p2, p3)
compute(r1, r2, r3)

