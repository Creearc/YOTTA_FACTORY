import requests
import json

SERVER_IP = 'http://127.0.0.1:8081'
KEY = 'a524580d-1344-4efb-a35e-e07c9d5b0ec2'

def ask(url, question_text):
  url = '{}/question'.format(url)
  data = {'question' : question_text}
  response = requests.post(url=url, json=data)
  out = response.json()
  return out
