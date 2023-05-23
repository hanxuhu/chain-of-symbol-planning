import json
f = open('shuffle_both_result3.json')
data= json.load(f)
#data = data['']
import re


def parse(string):

    #string = "This is a string to remove brick and find the first letter after it. We also need to remove brick again."
    search_str = "(?i)remove .*?brick"
    start_index = 0
    res = ''
    matches = re.finditer(search_str, string)
    #print(list(matches))
    for match in matches:
       start_index = match.end()
       letter_index = start_index
       while letter_index < len(string) and not string[letter_index].isalpha():
          letter_index += 1
       if letter_index < len(string):
          #print("The first letter after 'remove brick' is:", string[letter_index])
          res = res + string[letter_index]
    result = re.sub(r'(\w+)\1+', r'\1', res)
    return result

i = 1
ac = 0
for item in data:
    pred = item['pred']
    print(i)

    res = parse(pred)
    print(pred)
    print('res',res)
    print('label',item['label'])
    if res == item['label'] or res == item['label'][:-1]or res[:-1]==item['label']:
       ac += 1
    i += 1
acc = ac/i
print('acc', acc)

        

