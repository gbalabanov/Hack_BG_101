import requests


class GHInfo:

    URL = "https://api.github.com/users/?"
    URL_followers = "https://api.github.com/users/?/followers"
    URL_following = "https://api.github.com/users/?/following"
    header = {"client_id": "e7fa7529c9af0e814361",
              "client_secret": "a6526713d18d647258be57feb17fe727db1a4901",
              "page": ""}

    def _get_followers(self, name):
        followers = []
        try:
            temp = requests.get(GHInfo.URL.replace("?", name), params = GHInfo.header).json()
            count = (temp["followers"] // 30) + 1
            for page in range(1, count + 1):
                GHInfo.header["page"] = page
                for x in requests.get(GHInfo.URL_followers.replace("?", name), params=GHInfo.header).json():
                    followers.append(x["login"])
            return followers, len(followers)
        except TypeError:
            print("No such account !")

    def _get_following(self, name):
        following = []
        try:
            temp = requests.get(GHInfo.URL.replace("?", name), params = GHInfo.header).json()
            count = (temp["following"] // 30) + 1
            for page in range(1, count + 1):
                GHInfo.header["page"] = page
                for x in requests.get(GHInfo.URL_following.replace("?", name), params=GHInfo.header).json():
                    following.append(x["login"])
            return following, len(following)
        except TypeError:
            print("No such account !")

    def __init__(self, acc_name):
        self._followers = self._get_followers(acc_name)
        self._following = self._get_following(acc_name)


g = GHInfo("radorado")
print(g._following)
