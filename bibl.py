import requests
import json

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

result = requests.get('https://{}/netscan'.format(BASE_URL),
                      headers={'authorization' : KEY})

print(result.json())
