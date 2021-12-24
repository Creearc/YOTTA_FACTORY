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


##result = requests.get('https://{}/factory/{}/map'.format(BASE_URL, ID),
##                      headers={'authorization' : KEY})
##
##print(result.json())

#result = requests.get('https://{}/netscan'.format(BASE_URL),
#                      headers={'authorization' : KEY})

#result = requests.get('https://{}/devices'.format(BASE_URL),
#                      headers={'authorization' : KEY})

#result = requests.get('https://{}/netscan'.format(BASE_URL),
#                      headers={'authorization' : KEY})


'''

player_server = 'c3ac:c93e:92b7:f23a:6fc4:69e6:ff43:3682'
attack_server = '706a:8991:c346:997a:64ed:6130:ed74:f78e'


result = requests.post( url='https://{}/devices/{}'.format(BASE_URL, player_server),
                        headers={'authorization' : KEY,
                                 'content-type' : 'application/json'},
                        json = {"actionType": "attack","targetIp": attack_server})  
'''

server_up = 'c089:e9f1:98fb:44b1:8399:438a:99e4:e3db'
#attack_server = '2229:e7f8:8b3c:a4ef:644f:cb04:c6f6:52b0bbb'

#'''
result = requests.post( url='https://{}/devices/{}'.format(BASE_URL, server_up),
                        headers={'authorization' : KEY,
                                 'content-type' : 'application/json'},
                        json = {"actionType": "question"})
#'''

#ans = requests.post( url='https://{}/devices/{}'.format(BASE_URL, server_up),
#                        headers={'authorization' : KEY,
#                                 'content-type' : 'application/json'},
#                        json = {"actionType": "upgrade",
#                                "questionId": "1ec64b2a-614c-6188-9e29-d179651b1c49",
#                                "answers": ["1ec64b2a-614c-63cc-9fcd-d179651b1c49"]})

#ans = requests.post( url='https://{}/devices/{}'.format(BASE_URL, server_up),
#                        headers={'authorization' : KEY,
#                                 'content-type' : 'application/json'},
#                        json = {"actionType": "upgrade",
#                                "questionId": "1ec64b2a-614c-6188-9e29-d179651b1c49",
#                                "answers": ["1ec64b2a-614c-63cc-9fcd-d179651b1c49"]})

#print(result.json())
pprint.pprint(result.json(), width=4)
print("  ")
#pprint.pprint(ans.json(), width=4)