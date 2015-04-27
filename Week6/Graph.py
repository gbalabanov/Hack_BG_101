class Graph:

    def __init__(self):
        self.nodes = {}

    def add_node(self,node):
        self.nodes[node]=set()
        return True

    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes[node1]:
            self.nodes[node1].add(node2)
            return True
        else:
            return False

    def get_neighbours_for(self, node):
        return self.nodes[node]

    def path_between(self, node1, node2):
        queue = [[node1]]
        visited = set()
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == node2:
                return len(path) - 1
            elif node not in visited and node in self.nodes:
                for current_neighbour in self.nodes[node]:
                    new_path = list(path)
                    new_path.append(current_neighbour)
                    queue.append(new_path)
            visited.add(node)
        return False



a=Graph()
a.add_edge("a1","a2")
a.add_edge("a2","a3")
a.add_edge("a2","a4")
a.add_edge("a4","a5")
a.add_edge("a5","a6")
a.add_edge("a6","a7")
print(a.nodes)
print(a.path_between("a1","a5"))
