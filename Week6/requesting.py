import requests

r = requests.get("https://api.github.com/users/radorado?client_id=e7fa7529c9af0e814361&client_secret=a6526713d18d647258be57feb17fe727db1a4901")
followers=[]
for x in requests.get((r.json()["followers_url"])+"?client_id=e7fa7529c9af0e814361&client_secret=a6526713d18d647258be57feb17fe727db1a4901").json():
    followers.append(x["login"])
print(followers)
