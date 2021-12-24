import requests
import json
import pprint
import time

BASE_URL = 'api-yofactory.dats.team'
ID = '01FQP5MPMP7QPKANH2FZQJNV0Z'
KEY = 'a524580d-1344-4efb-a35e-e07c9d5b0ec2'

def scan_map():
  result = requests.get('https://{}/factory/{}/map'.format(BASE_URL, ID),
                        headers={'authorization' : KEY})

  return result.json()

def netscan():
  result = requests.get('https://{}/netscan'.format(BASE_URL),
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

def openn(idd='ee7f:4e3f:8236:67d4:fe08:af2:6acf:ebaf'):
  result = requests.post( url='https://{}/devices/{}'.format(BASE_URL, idd),
                        headers={'authorization' : KEY,
                                 'content-type' : 'application/json'},
                        json = {"actionType": "open"})
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


#pprint.pprint(scan_map()['fields'][122])
#pprint.pprint(attack())




##while True:
##  d_s = []
##  n_s = []
##
####d = devices()['devices']
####for key in d.keys():
####  element = d[key]
####  print(element['ip'], element['position'])
####
####while True:
####  net = netscan()['netscan']
####  key = 'c3ac:c93e:92b7:f23a:6fc4:69e6:ff43:3682'
####  for k in net[key].keys():
####    element = net[key][k]
####    for i in range(5):
####      print(attack(key, k))
####      time.sleep(0.2)

##
##  for i in d_s:
##    for j in n_s:
##      if i == j:
##        continue
##      print(attack(i, j))
##      time.sleep(0.5)



##net = netscan()['netscan']
##for key in net.keys():
##  mn = 0
##  mn_ip = None
##  for k in net[key].keys():
##    element = net[key][k]
##    print(element['type'], element['ip'], element['position'], element['SLC'])
##
##  print('______')



#print(openn('3f9f:188c:d48f:cc55:8957:938b:25b6:3d09'))

while True:
  d = devices()['devices']
  drone_id = '43dd:52a1:61c:d829:a8ec:bd05:23d4:284b'
  x, y = d[drone_id]['position']['x'], d[drone_id]['position']['y']

  print(move(x=x-1, y=y, idd=drone_id))
  time.sleep(0.2)
