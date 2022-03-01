import requests

url = "http://api.open-notify.org/astros.json"

reponse = requests.get(url)
contenu = reponse.json()
print(contenu)

