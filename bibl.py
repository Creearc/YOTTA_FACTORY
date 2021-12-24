import requests
import json
import pprint

BASE_URL = 'api-yofactory.dats.team'
ID = '01FQP5MPMP7QPKANH2FZQJNV0Z'
KEY = 'a524580d-1344-4efb-a35e-e07c9d5b0ec2'

def scan_map():
  result = requests.get('https://{}/factory/{}/map'.format(BASE_URL, ID),
                        headers={'authorization' : KEY})

  return result.json()

def devices():
  result = requests.get('https://{}/devices'.format(BASE_URL),
                      headers={'authorization' : KEY})

  return result.json()

def move(x=57, y=135, idd='ee7f:4e3f:8236:67d4:fe08:af2:6acf:ebaf'):
  result = requests.post( url='https://{}/devices/{}'.format(BASE_URL, idd),
                        headers={'authorization' : KEY,
                                 'content-type' : 'application/json'},
                        json = {"actionType": "move",
                                "x": x,
                                "y": y})
  return result.json()

def attack(player_server='ee7f:4e3f:8236:67d4:fe08:af2:6acf:ebaf',
           attack_server='2229:e7f8:8b3c:a4ef:644f:cb04:c6f6:52b0'):
  result = requests.post( url='https://{}/devices/{}'.format(BASE_URL, player_server),
                        headers={'authorization' : KEY,
                                 'content-type' : 'application/json'},
                        json = {"actionType": "attack",
                                "targetIp": attack_server
                                })
  return result.json()


#pprint.pprint(scan_map()['fields'][135])
pprint.pprint(attack())


