import requests
import json
import pprint

BASE_URL = 'api-yofactory.dats.team'
ID = '01FQP5MPMP7QPKANH2FZQJNV0Z'
KEY = 'a524580d-1344-4efb-a35e-e07c9d5b0ec2'

def ask(url, data):
  response = requests.post(url=url, params=data)
  out = response.content
  return out

'''
player_server = 'ee7f:4e3f:8236:67d4:fe08:af2:6acf:ebaf'
attack_server = '63e2:b26b:d65d:c39b:d659:e657:73f8:f6d2'


result = requests.post( url='https://{}/devices/{}'.format(BASE_URL, player_server),
                        headers={'authorization' : KEY,
                                 'content-type' : 'application/json'},
                        json = {"actionType": "attack","targetIp": attack_server})  

pprint.pprint(result.json(), width=4)
'''

server_up = 'c089:e9f1:98fb:44b1:8399:438a:99e4:e3db'
ans = requests.post( url='https://{}/devices/{}'.format(BASE_URL, server_up),
                        headers={'authorization' : KEY,
                                 'content-type' : 'application/json'},
                        json = {"actionType": "upgrade",
                                "questionId": "1ec64b2a-6153-6866-b197-d179651b1c49",
                                "answers": ["1ec64b2a-6153-68b6-a2cf-d179651b1c49"]})

pprint.pprint(ans.json(), width=4)
#'''