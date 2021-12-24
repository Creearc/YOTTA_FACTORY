import requests
import json
import pprint
import time

BASE_URL = 'api-yofactory.dats.team'
ID = '01FQP5MPMP7QPKANH2FZQJNV0Z'
KEY = 'a524580d-1344-4efb-a35e-e07c9d5b0ec2'

my_key = '4e80:4734:5974:7d70:56d2:8e53:ca22:6640'

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

while True:
  d = devices()['devices']
  delay = 0.11
  
  for i in range(3):
    try:
      net = netscan()['netscan']
      for key in net.keys():
        if key == 'ee7f:4e3f:8236:67d4:fe08:af2:6acf:ebaf':
          if i == 0:
            mn_ip = 'b452:8512:7e84:2ee1:2efa:106a:3a45:38e2'
            print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
            time.sleep(delay)
            continue
          else:
            mn_ip = 'c089:e9f1:98fb:44b1:8399:438a:99e4:e3db'
            print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
            time.sleep(delay)
            continue

            
##        elif key == 'b452:8512:7e84:2ee1:2efa:106a:3a45:38e2':
##          if i == 0:
##            mn_ip = '54c0:f78d:94c4:b06c:83e8:48b1:794d:be75'
##            print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##            time.sleep(delay)
##            continue
##          else:
##            mn_ip = 'c089:e9f1:98fb:44b1:8399:438a:99e4:e3db'
##            print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##            time.sleep(delay)
##            continue
##        
##        elif key == 'c089:e9f1:98fb:44b1:8399:438a:99e4:e3db':
##          mn_ip = '54c0:f78d:94c4:b06c:83e8:48b1:794d:be75'
##          print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##          time.sleep(0.12)
##          continue
##        elif key == '54c0:f78d:94c4:b06c:83e8:48b1:794d:be75':
##          mn_ip = 'c3ac:c93e:92b7:f23a:6fc4:69e6:ff43:3682'
##          print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##          time.sleep(0.12)
##          continue
##        elif key == 'c3ac:c93e:92b7:f23a:6fc4:69e6:ff43:3682':
##          mn_ip = '706a:8991:c346:997a:64ed:6130:ed74:f78e'
##          print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##          time.sleep(0.12)
##          continue
##        
##        elif key == '706a:8991:c346:997a:64ed:6130:ed74:f78e':
##          if i == 0:
##            mn_ip = '6bac:6f1c:bf2a:9f0a:bf4c:22e9:4187:9eef'
##            print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##            time.sleep(0.12)
##            continue
##          else:
##            mn_ip = 'b76e:c5ec:130b:a242:f326:71ca:e742:756'
##            print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##            time.sleep(0.12)
##            continue
##
##        
##        elif key == 'b76e:c5ec:130b:a242:f326:71ca:e742:756':
##          mn_ip = '956c:1d2a:bd80:5384:55d4:72e0:8fc2:3723'
##          print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##          time.sleep(0.12)
##          continue
##        elif key == '956c:1d2a:bd80:5384:55d4:72e0:8fc2:3723':
##          mn_ip = 'd258:e370:bf64:da:297c:6dfd:85f8:41f9'
##          print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##          time.sleep(0.12)
##          continue
##        elif key == 'd258:e370:bf64:da:297c:6dfd:85f8:41f9':
##          mn_ip = '700c:f4e6:61e3:35fc:b327:788d:68c2:d18'
##          print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##          time.sleep(0.12)
##          continue
##        elif key == '700c:f4e6:61e3:35fc:b327:788d:68c2:d18':
##          mn_ip = 'f87:91a5:ef7c:e2ec:7f16:7f4a:3e94:4b1c'
##          print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##          time.sleep(0.12)
##          continue
##
##
##        
##        elif key == '8c:4e68:a4e0:9eea:c55c:e95a:d56e:e1fb':
##          mn_ip = 'b452:8512:7e84:2ee1:2efa:106a:3a45:38e2'
##          print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
##          time.sleep(0.12)
##          continue
  ##      elif key == '1d0:b781:b950:d126:bebb:8943:90e2:89a8':
  ##        mn_ip = 'fd99:9a46:fe8e:6c82:4665:b3c8:8c2c:889a'
  ##        print(attack(key, mn_ip), mn_ip, net[key][mn_ip]['SLC'])
  ##        time.sleep(0.12)
  ##        continue    
        
        mn = 100
        mx_y = 200
        mn_ip = None
        mx_ip = None
        for k in net[key].keys():
          element = net[key][k]
          if element['type'] != 'factory_server':
            continue
          if (mn_ip is None or mn > element['SLC']) and element['userIp'] == my_key:
            mn = element['SLC']
            mn_ip = element
          if (mx_ip is None or element['position']['y'] > mx_y) and element['userIp'] == my_key:
            mx_y = element['position']['y']
            mx_ip = element
            
        if mn < 30 and mn_ip['userIp'] == my_key:
          print('heal', attack(key, mx_ip['ip']), mx_ip['ip'], mx_ip['SLC'])
        else:
          print('attack', attack(key, mn_ip['ip']), mn_ip['ip'], mn_ip['SLC'])
        time.sleep(0.12)
    except Exception as e:
      print(e)
      continue
