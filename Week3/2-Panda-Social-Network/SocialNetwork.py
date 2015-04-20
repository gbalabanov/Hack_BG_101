from Panda import Panda
from custom_exceptions import PandaAlreadyThere
from custom_exceptions import PandasAlreadyThere
import csv
import json


class SocialNetwork():

    def __init__(self):
        self.database = {}

    def add_panda(self, panda):
        if panda in self.database:
            raise PandaAlreadyThere
        else:
            self.database[panda] = []

    def has_panda(self, panda):
        return panda in self.database

    def make_friends(self, panda1, panda2):
        pan1_in_2 = False
        pan2_in_1 = False
        if panda1 in self.database:
            if panda2 in self.database[panda1]:
                pan2_in_1 = True
        if panda2 in self.database:
            if panda1 in self.database[panda2]:
                pan1_in_2 = True
        if pan1_in_2 and pan2_in_1:
            raise PandasAlreadyThere
        if panda1 not in self.database:
            self.database[panda1] = []
        if panda2 not in self.database:
            self.database[panda2] = []
        self.database[panda1].append(panda2)
        self.database[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda1 in self.database and panda2 in self.database:
            return panda2 in self.database[panda1] and panda1 in self.database[panda2]
        return False

    def friends_of(self, panda):
        if panda not in self.database:
            return False
        return self.database[panda]

    def connection_level(self, panda1, panda2):
        queue = [[panda1]]
        visited = set()
        if panda1 not in self.database or panda2 not in self.database:
            return False
        while queue:
            path = queue.pop(0)
            panda = path[-1]
            if panda == panda2:
                return len(path) - 1
            elif panda not in visited:
                for current_neighbour in self.database.get(panda):
                    new_path = list(path)
                    new_path.append(current_neighbour)
                    queue.append(new_path)
            visited.add(panda)
        return -1

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) > 0:
            return True
        return False

    def save_readable(self, fileName):
        frList = ""
        with file(fileName, "w") as f:
            for x, y in self.database.items():
                for panda in y:
                    frList += panda.name() + ", "
                f.write(str(x) + " has friends: " + frList)
                f.write("\n\n")
                frList = ""

    def save_csv(self, filename):
        writer = csv.writer(open(filename, 'wb'))
        for key, value in self.database.items():
            #friends = [x for x in value]
            writer.writerow([key, value])

    def save_json(self, filename):
        json_string = ""
        for panda in self.database:
            json_string += panda.serialize()
            for friend in self.database[panda]:
                json_string += friend.serialize()
            json_string += "\n"
        with open(filename, mode="w") as f:
            f.write(json_string)

    """def load_json(self,filename):
        with open(filename,"r") as f:
            content=f.read()
        return json.loads(content) """

    def read_csv(self, filename):
        reader = csv.reader(open(filename, "rb"))
        self.database = dict(line for line in reader)


a = Panda("Gosho", "asd@ad.bg", "male")
b = Panda("Pesho", "asd@ad.bg", "male")
c = Panda("Misho", "asd@ad.bg", "male")
d = Panda("Sasho", "asd@ad.bg", "male")
e = Panda("Tisho", "asd@ad.bg", "male")
sn = SocialNetwork()
sn.make_friends(a, b)
sn.make_friends(b, c)
sn.make_friends(c, d)
sn.make_friends(d, e)
#sn.make_friends(b, d)
#sn.make_friends(a, d)
print(sn.connection_level(a, e))
sn.save_csv("output.csv")
sn2 = SocialNetwork()
sn2.read_csv("output.csv")
print(sn.database)
print()
print(sn2.database)
# print(sn2.load_json("output.json"))
