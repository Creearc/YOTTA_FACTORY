import json
from pprint import pprint


with open(r"data.json", "r", encoding='utf-8') as f:
    data = json.load(f)

words = []

for key in data.keys():
    words.append(key)

sort_word = sorted(words, key=len)
#sort_word.reverse()


for word in sort_word:
    for word2 in sort_word:
        for word3 in sort_word:
            for word4 in sort_word:
                if word == word2 or word2 == word3 or word3 == word4 or word == word4:
                    continue

                if word[-1] == word2[0] and word[0] == word4[0] and word4[-1] == word3[0] and word3[-1] == word2[-1]:
                    print(word, word2, word3, word4)
                    
