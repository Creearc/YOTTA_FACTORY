import requests
import json

SERVER_IP = 'http://127.0.0.1:8081'
KEY = ''

def ask(url, question_text):
  url = '{}/question'.format(url)
  data = {'question' : question_text}
  response = requests.post(url=url, json=data)
  out = response.json()
  return out
