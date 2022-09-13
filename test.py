import requests
import json
from pprint import pprint
import time

from word3 import data

TOKEN = 'QilxtiFyW3wvUE12N1ClKdsejTpShfFA/aG33kJOPJ3zdZe9tRrqFrUdFRaBgb48zSs='

link = 'https://dtower-api.datsteam.dev/towers/{id}'


def top():
  result = requests.get(url='https://dtower-api.datsteam.dev/towers/top')
  return result.content


def status(idd):
  result = requests.get(url='https://dtower-api.datsteam.dev/towers/{id}'.format(id=idd),
                        headers={'token' : TOKEN,
                                 'content-type' : 'application/json'})
  return result.content


def build(data):
  result = requests.post(url='https://dtower-api.datsteam.dev/towers/',
                        headers={'token' : TOKEN,
                                 'content-type' : 'application/json'},
                        json = data)
  return result.content


idd = 'pavel_and_nikita_was_here_rtyrty6'

data = {
  "towerId": idd,
  "letters": data
}

pprint(build(data))

print(time.ctime())

while True:
    print(status(idd))
    time.sleep(5.0)

#pprint(top())
