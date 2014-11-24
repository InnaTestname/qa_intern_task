import requests
import json

url = "http://qainterview.cogniance.com/"
payload = {'name':'Inna', 'position':'QA engineer'}
headers = {'content-type':'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)

print r.status_code
#print r.name
print r.content
print r.text
#print r.position
#code that verifies that data is added to server
#not sure
#assert r.name == 'Inna', "Your name wasn't added to the server"
#assert r.position == 'QA Engineer', "Your position wasn't added to the server"

#code that verifies correctness of returned response code
assert r.status_code == 200, 'Request is wrong, status_code is ' + str(r.status_code) #or r.status_int == 200

