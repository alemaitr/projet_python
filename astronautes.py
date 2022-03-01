import requests

url = "http://api.open-notify.org/astros.json"

reponse = requests.get(url)
contenu = reponse.json()
# print(contenu['people'])
for qui in contenu['people'] :
    if qui['craft'] == "ISS":
        print(qui["name"])



