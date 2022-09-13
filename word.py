


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


##word = 'притоносодержательница'.upper()
##for i in range(len(word)):
##    tmp = {"name" : word[i], "x" : 0, "y" : 0, "z" : len(word) - i - 1}
##    data.append(tmp)
##
##
##word = 'трансформаторостроение'.upper()
##for i in range(len(word)):
##    tmp = {"name" : word[i], "x" : 2, "y" : 0, "z" : len(word) - i - 1}
##    data.append(tmp)
##
##word = 'пот'.upper()
##for i in range(len(word)):
##    tmp = {"name" : word[i], "x" : len(word) - i - 1, "y" : 0, "z" : 21}
##    data.append(tmp)
##    #print(tmp)
##
##word = 'человеконенавистничество'.upper()
##for i in range(len(word)):
##    tmp = {"name" : word[i], "x" : 1, "y" : 0, "z" : 21 + len(word) - i - 1}
##    data.append(tmp)
##    #print(tmp)
##
###print(data)


word = 'катер'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : len(word) - i - 1, "y" : 1, "z" : 19}
    data.append(tmp)
    #print(tmp)

word = 'капер'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 1, "y" : len(word) - i - 1, "z" : 19}
    data.append(tmp)
    #print(tmp)

word = 'ведро'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 3, "y" : len(word) - i - 1, "z" : 19}
    data.append(tmp)
    #print(tmp)

word = 'дебри'.upper()
for i in range(len(word)):
    tmp = {"name" : word[i], "x" : len(word) - i - 1, "y" : 3, "z" : 19}
    data.append(tmp)
    #print(tmp)

    
    
i = 0
while i < len(data):
    j = 0
    while j < len(data):
        if i == j:
            j += 1
            continue
        if data[i]['x'] == data[j]['x'] and data[i]['y'] == data[j]['y'] and data[i]['z'] == data[j]['z']:
            data.pop(i)
            print(i)
        else:
            j += 1
    i += 1

print(data)



