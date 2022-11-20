


data = {
#  "towerId": idd,
  "letters": [
    {
      "name": "К",
      "x": 0,
      "y": 0,
      "z": 0
    },
    {
      "name": "О",
      "x": 1,
      "y": 0,
      "z": 0
    },
    {
      "name": "Т",
      "x": 2,
      "y": 0,
      "z": 0
    }
  ]
}


word = 'человеконенавистничество'.upper()

data = []


##for i in range(len(word)):
##    tmp = {"name" : word[i], "x" : 0, "y" : 0, "z" : len(word) - i - 1}
##    data.append(tmp)


word = 'притоносодержательница'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 0, "y" : 0, "z" : len(word) - i - 1}
    data.append(tmp)


word = 'трансформаторостроение'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 2, "y" : 0, "z" : len(word) - i - 1}
    data.append(tmp)

word = 'пот'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : len(word) - i - 1, "y" : 0, "z" : 21}
    data.append(tmp)
    #print(tmp)

word = 'человеконенавистничество'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 1, "y" : 0, "z" : 21 + len(word) - i - 1}
    data.append(tmp)
    #print(tmp)

#print(data)


data_out = []
for i in range(len(data)):
    for j in range(len(data)):
        if i == j:
            continue
        if data[i] == data[j]:
            data_out.append(data[i])
            
data = data_out
print(data)


#---------------------------------------------------------------------------------------------
word = 'кинодокументалистика'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 1, "y" : 0, "z" : len(word) - i - 1}
    data.append(tmp)

word = 'кораблестроительство'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 0, "y" : 1, "z" : len(word) - i - 1}
    data.append(tmp)



word = 'выкристаллизовывание'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 3, "y" : 0, "z" : len(word) - i - 1}
    data.append(tmp)

word = 'двадцатипятирублёвка'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 0, "y" : 3, "z" : len(word) - i - 1}
    data.append(tmp)



word = 'революционизирование'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 4, "y" : 1, "z" : len(word) - i - 1}
    data.append(tmp)

word = 'распространительница'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 1, "y" : 4, "z" : len(word) - i - 1}
    data.append(tmp)



word = 'индивидуализирование'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 4, "y" : 3, "z" : len(word) - i - 1}
    data.append(tmp)

word = 'одиннадцатиклассница'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 3, "y" : 4, "z" : len(word) - i - 1}
    data.append(tmp)
    
#---------------------------------------------------------------------------------------------
word = 'выкристаллизовывание'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 1, "y" : 0, "z" : len(word) - i - 1}
    data.append(tmp)

word = 'одиннадцатиклассница'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 0, "y" : 1, "z" : len(word) - i - 1}
    data.append(tmp)
