import re
text = "To get brick N, first remove brick F, then remove brick U, and finally remove brick N."#"From cinema G, the nearest school is school D which is 100 meters away. So, to reach the nearest school, you need to take the road from cinema G to school D. Therefore, the sequence of landmarks to reach the nearest school from the start point is cinema G, school D."
text_list = text.split(".")
print(text_list)

uppercase_letters = ""
target_sentence = text_list[-1] if text_list[-1] != '' else text_list[-2]
for char in target_sentence:
    if char.isupper():
        uppercase_letters += char
uppercase_letters = uppercase_letters[1:]
if uppercase_letters[0] == uppercase_letters[-1]:
    uppercase_letters = uppercase_letters[1:]
print(uppercase_letters)

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

s1 = "abcdefg"
s2 = "defghij"
print(longest_common_substring(s1, s2)) # 
