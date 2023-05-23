import json
import re
#f_cos = open('cos_prompt_results/shuffle_both_result_cos.json')
#f_cot = open('cot_prompt_results/shuffle_descp_result.json')
data_final = []
step = 0
index_cos = []

for i in range(1):
   f_path = 'chatgpt_results/nlvr_results/result_chinese.json'.format(i)
   f_cos = open(f_path)
   data_cos= json.load(f_cos)
   data_final += data_cos
ac = 0
p = 0
r = 0
word_map = {
       "black": "黑色",
       "yellow": "黑色",
       "white": "黑色",
       "blue": "黑色",
       "triangle": "三角形",
       "square": "正方形",
       "round": "圆形",
       "small": "小",
       "middle": "中等大小",
       "large": "大",
       "left": "左",
       "right": "右",
}
for data in data_final:
   step+=1
   res = data['label']
   mapped_res = []
   for word_list in res:
       mapped_words = []
       for word in word_list[:-1]:
         mapped_word = word_map.get(word, word)
         mapped_words.append(mapped_word)
       mapped_words.reverse()
       mapped_res.append(mapped_words)
   print(res)
   print(mapped_res)
  
   #for item in res:
   #   x = item[0]
   #   item[0] = item[2]
   #   item[2] = x
   
   res_str = set()
   #print(res)
   for item in mapped_res:
     res_str.add(str(item))
   #pattern = r"\(([^,]+),\s*([^,]+),\s*([^)]+)\)\s+(left|middle|right)"
   #matches = re.findall(pattern,data['pred'])
   pattern = pattern = r'（([\u4e00-\u9fa5]+)，([\u4e00-\u9fa5]+)，([\u4e00-\u9fa5]+)）'
   #pattern = r'(小|大|中等大小,三角形|正方形|圆形,黑色|白色|黄色|蓝色)'
   matches = re.findall(pattern, data['pred'])
   #print(data['pred'])
   #print('matches', matches)
   matches = [str(list(match)) for match in matches]
   print('matches', matches)
   while i <len(matches)-2:
      if matches[i] == matches[i+1]:
         del matches[i] 
         del matches[i]
         i-=2
      i+=1
   pred_set = set(matches)
   print(pred_set)
   print(res_str)
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
     if overlap_count == len(res_str):
        ac+=1
     else:
        index_cos.append(step)
     p += overlap_count/ (len(pred_set)/2)
     r += overlap_count/ (len(res_str))

p_all = p/len(data_final)
r_all = r/len(data_final)
ac_all = ac/len(data_final)
print('precision', p_all)
print('recall', r_all)
print('acc', ac_all)
print(len(data_final))
'''


data_final = []
index_cot = []
step = 0
for i in range(9):
   f_path = 'cot_nlvr_results/result{}.json'.format(i)
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
    #print(moves) # Output: ['1. Move the small triangle in black from the middle box to the right box.', '2. Move the small square in black from the middle box to the right box.', '3. Move the large round in black from the middle box to the right box.']
    for sentence in moves:
        #Split the sentence into words
        words = sentence.split()
        if len(words)!=14:
           continue
        # Remove any punctuation or capitalization from the words
        words = [w.lower().strip(",.") for w in words]
        # Map each word to its desired format using the dictionary
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
     if overlap_count == len(res_str):
        ac+=1
     else:
        index_cot.append(step)
     p += overlap_count/ (len(pred_set) + len(pred_other))
     r += overlap_count/ (len(res_str))
p_all = p/len(data_final)
r_all = r/len(data_final)
ac_all = ac/len(data_final)
print('precision', p_all)
print('recall', r_all)
print('acc', ac_all)
print(len(data_final))
print(index_cos)
print(index_cot)


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
    "box": None
}
data_final = []
for i in range(1):
   f_path = 'baseline_results/result{}.json'.format(i)
   f_cos = open(f_path)
   data_cos= json.load(f_cos)
   data_final += data_cos
ac = 0
p = 0
r = 0
for data in data_final[:20]:
   res = data['label']
   res_str = set()
   print(res)
   pred_sentencese = data['pred'].split('\n')
   flag = True
   pred_parsed = []
   for sentence in pred_sentencese:
      sentence_list = sentence.split('')
      if sentence_list[0]!='Open'
      pred_single_sentence = []
      for word in sentence_list:
         if word in word_map.keys():
            pred_single_sentence.append(word_map[word])
      print(pred_single_sentence)
      pred_parsed.append(str(pred_single_sentence))
      
            
        
     res_str.add(str(item))
   pattern = r'\((black|white|yellow|blue),\s(triangle|square|round),\s(small|large|middle),\s(middle|right|left)\)'
   matches = re.findall(pattern, data['pred'])
   matches = [str(list(match)) for match in matches]
   while i <len(matches)-1:
      if matches[i] == matches[i+1]:
         del matches[i] 
         del matches[i]
         i-=2
      i+=1
   pred_set = set(matches)
   print(pred_set)
   print(res_str)
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
     print('overlap_count', overlap_count)
     print('res_set', len(res_str))
     if overlap_count == len(res_str):
        ac+=1
     p += overlap_count/ (len(pred_set)/2)
     r += overlap_count/ (len(res_str))

p_all = p/len(data_final)
r_all = r/len(data_final)
ac_all = ac/len(data_final)
print('precision', p_all)
print('recall', r_all)
print('acc', ac_all)
print(len(data_final))
'''