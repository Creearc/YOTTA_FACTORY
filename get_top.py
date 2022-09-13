import requests
import json
from pprint import pprint
import time

TOKEN = 'QilxtiFyW3wvUE12N1ClKdsejTpShfFA/aG33kJOPJ3zdZe9tRrqFrUdFRaBgb48zSs='

def top():
  result = requests.get(url='https://dtower-api.datsteam.dev/towers/top')
  return result.content


while True:
    pprint(top())
    time.sleep(60.0)
