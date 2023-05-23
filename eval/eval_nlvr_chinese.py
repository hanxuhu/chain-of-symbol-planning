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
