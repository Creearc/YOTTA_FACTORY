import requests
import json
import pprint
import time
import math

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
  coords = []
  my_servers = dict()
  servs_to_heal = set()
  

  d = devices()['devices']
  for key in d.keys():
    element = d[key]
    if element['type'] == 'drone':
      x, y = d[key]['position']['x'], d[key]['position']['y']
      coords.append((x, y))
    elif element['type'] != 'door':
      x, y, t = d[key]['position']['x'], d[key]['position']['y'], d[key]['targetIp']
      my_servers[element['ip']] = (x, y, t)
  delay = 0.11
  
  for i in range(1):
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
        
        mn = 100
        mx_dist = 0
        mn_ip = None
        mx_ip = None
        drone_attack = False
        
        for k in net[key].keys():
          element = net[key][k]
          if element['type'] == 'drone' or element['type'] == 'door':
            continue
          
          for c in coords:
            if element['userIp'] != my_key:
              if abs(element['position']['x'] - c[0]) < 2 and abs(element['position']['y'] - c[1]) < 2:
                if my_servers[key][0] != element['ip']:
                  print('drone attack', attack(key, element['ip']), element['ip'], element['SLC'])
                  time.sleep(0.12)
                drone_attack = True
                

          if drone_attack:
            break
          
          if element['userIp'] == my_key:
            if mn_ip is None or mn > element['SLC']:
              mn = element['SLC']
              mn_ip = element
              if mx_ip is None:
                mx_ip = mn_ip
              
          else:
            dist = math.sqrt((my_servers[key][0] - element['position']['x']) ** 2 + (my_servers[key][1] - element['position']['y']) ** 2)
            if mx_ip is None or mx_dist < dist:
              mx_dist = dist
              mx_ip = element
              if mn_ip is None:
                mn_ip = mx_ip

        if drone_attack:
          continue
          
        if mn < 40 and not(mn_ip['ip'] in servs_to_heal):
          if my_servers[key][0] != mn_ip['ip']:
            print('heal', attack(key, mn_ip['ip']), mn_ip['ip'], mn_ip['SLC'])
            servs_to_heal.add(mn_ip['ip'])
            time.sleep(0.12)
        else:
          if my_servers[key][0] != mx_ip['ip']:
            print('attack', attack(key, mx_ip['ip']), mx_ip['ip'], mx_ip['SLC'])
            time.sleep(0.12)
        
    except Exception as e:
      print(e)
      continue
