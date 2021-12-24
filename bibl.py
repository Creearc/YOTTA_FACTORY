import requests
import json

SERVER_IP = 'https://api-yofactory.dats.team/'
ID = 'https://yofactory.dats.team/?id=01FQP5MPMP7QPKANH2FZQJNV0Z'
KEY = 'a524580d-1344-4efb-a35e-e07c9d5b0ec2'

def ask(url, question_text):
  url = '{}/question'.format(url)
  data = {'question' : question_text}
  response = requests.post(url=url, json=data)
  out = response.json()
  return out
