class Histogram:

    def __init__(self):
        self.database = {}

    def add_server(self, server):
        if server not in self.database:
            self.database[server] = 1
        else:
            self.database[server] += 1

    def count(self, server):
        if server not in self.database:
            return "No such server in the database !"
        return self.database[server]

    def get_dict(self):
        return self.database
