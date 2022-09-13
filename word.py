


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

for i in range(len(word)):
    tmp = {"name" : word[i], "x" : 0, "y" : 0, "z" : len(word) - i - 1}
    data.append(tmp)
    #print(tmp)

#print(data)
