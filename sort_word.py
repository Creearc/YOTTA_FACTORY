import json
from pprint import pprint


with open(r"data.json", "r", encoding='utf-8') as f:
    data = json.load(f)

words = []

for key in data.keys():
    words.append(key)

sort_word = sorted(words, key=len)
sort_word.reverse()

pprint(sort_word)

#for word in sort_word:
#    with open(r"words.txt", "a") as f:
#        f.write(word + '\n')