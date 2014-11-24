import requests
import json

url = "http://qainterview.cogniance.com/"
payload = {'name':'Inna', 'position':'QA engineer'}
headers = {'content-type':'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers) 

def make_request():
	response_code = r.status_code
	return response_code

def check_added_data():
	added_name = r.name
	added_position = r.position
	return added_name, added_position

def test_function():
	assert make_request() == 200
	assert check_added_data == ('QA Engineer', 'Inna')



