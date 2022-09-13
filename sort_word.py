import json
from pprint import pprint


with open(r"data.json", "r", encoding='utf-8') as f:
    data = json.load(f)

words = []

for key in data.keys():
    words.append(key)

sort_word = sorted(words, key=len)
sort_word.reverse()

#pprint(sort_word)
for word in sort_word:
    if word[len(word)-1] == 'ё':
        print(word)

#for word in sort_word:
#    if word[len(word)-1] != 'ь':
#        with open(r"words.txt", "a") as f:
#            f.write('{} {}\n'.format(len(word), word))