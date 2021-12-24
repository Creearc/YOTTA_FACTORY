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
##  arr = dict()
##
##  net = netscan()['netscan']
##  for key in net.keys():
##    arr[key] = set(net[key].keys())
##    
##  print(arr.keys())
##
##  for key_0 in arr.keys():
##    res = set(arr[key_0])
##    for key in arr.keys():
##      if key_0 == key:
##        continue
##      res = res.intersection(arr[key])
##    res = set(res)
##    for r in res:
##      for key in arr.keys():
##        print(attack(key, r))
##        time.sleep(0.2)


##print(attack('ee7f:4e3f:8236:67d4:fe08:af2:6acf:ebaf',
##             ''))

d = devices()['devices']
for key in d.keys():
   element = d[key]
   print(element['type'], element['ip'], element['position'], element['SLC'])

while True:
  net = netscan()['netscan']
  for key in net.keys():
    if key == 'ee7f:4e3f:8236:67d4:fe08:af2:6acf:ebaf':
      mn_ip = '539d:f078:1933:c8da:9377:5a00:c24c:272a'
      print(attack(key, mn_ip), mn_ip, element['SLC'])
      time.sleep(0.12)
      continue
    
    mn = 100
    mn_y = 200
    mn_ip = None
    for k in net[key].keys():
      element = net[key][k]
      if mn_ip is None or mn > element['SLC']:# or element['position']['y'] > mn_y:
      #if mn_ip is None or element['position']['y'] > mn_y:
        #mn_y = element['position']['y']
        mn = element['SLC']
        mn_ip = element['ip']
    
      print(attack(key, mn_ip), element['ip'], element['SLC'])
      time.sleep(0.12)
