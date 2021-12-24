import requests
import json

SERVER_IP = 'http://127.0.0.1:8081'

def ask(url, question_text):
  url = '{}/question'.format(url)
  data = {'question' : question_text}
  response = requests.post(url=url, json=data)
  out = response.json()
  return out

def ask2(question_text, result_type, component):
  response = requests.post(url=qanary_pipeline_url,
                             params={
                                 "question": question_text,
                                 "componentlist[]": component
                             }).json()
  result = get_final_result(result_type, response['endpoint'], response['inGraph'])
  return result
