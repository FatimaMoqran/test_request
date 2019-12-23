import requests
import json
from datetime import datetime
#r = requests.get('http://youtube.com')
#print(r.text) #affiche le contenu de la réponse
#print(r.json)
#print(r.headers)#affich les headres de la reponse sous forme de disctionnaire
#print(r.headers['Content-Type'])#affiche le content_type
response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)
print(response.json())

#donnees = json.dumps(response.json, sort_keys=True, indent=4)
parameters = {
    'lat': 40.71,
    'lon':-74
}
response2= requests.get('http://api.open-notify.org/iss-pass.json',params=parameters)
print(response2.json)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent= 4)
    print(text)

jprint(response2.json())

pass_times = response2.json()['response']
jprint(pass_times)

#extract only the risetime value
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

#convert these into easier to understand times
times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
