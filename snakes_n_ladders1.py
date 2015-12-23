__author__ = 'aiswarya'
class Queue:
    def __init__(self):
        self.q = []
        self.size = len(self.q)

    def put(self, a):
        self.q.append(a)
        self.size += 1

    def get(self):
        val = self.q[0]
        self.q = self.q[1:]
        self.size -= 1
        return val

    def empty(self):
        if self.size == 0:
            return True
        else:
            return False


class vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "WHITE"
        self.dist = None

    def addneighbour(self, key, weight=1):
        self.connectedTo[key] = weight

    def __str__(self):
        return self.id + 'connected to' + str(each.id for each in self.connectedTo)


class graph:
    def __init__(self):
        self.vertices = []
        self.num_vertices = len(self.vertices)

    def add_vertex(self, v):
        self.vertices.append(v)

    def find(self, key):
        for node in self.vertices:
            if node.id == key:
                return node
        return None

    def add_edge(self, start, end, weight=1):
        node = self.find(start)
        if end not in node.connectedTo.keys():
            node.connectedTo[end] = weight


    def freshen(self):
        for each_node in self.vertices:
            each_node.color = "WHITE"

    def print_graph(self):
        for each in self.vertices:
            print(each.id + " : " + str(each.connectedTo.keys()))

    def delete_all_edges(self, some_key):
        for each in self.vertices:
            if some_key in each.connectedTo.keys():
                del each.connectedTo[some_key]

    def replace_all_edges_to(self, key1, key2):
        for each in self.vertices:
            if key1 in each.connectedTo.keys():
                del each.connectedTo[key1]
                each.connectedTo[key2] = 1

    def drop_vertex(self, key):
        node = self.find(key)
        self.vertices.remove(node)


    def bfs(self, s_key, e_key):
        path = []
        s = self.find(s_key)
        path.append((s.id, 0))
        self.freshen()
        s.dist = 0
        Q = Queue()
        Q.put(s)
        while not Q.empty():
            curr_node = Q.get()
            for each_key in curr_node.connectedTo.keys():
                nbr = self.find(each_key)
                if nbr.color == "WHITE":
                    nbr.color = "GRAY"
                    nbr.dist = curr_node.dist + 1
                    Q.put(nbr)
                    path.append((nbr.id, nbr.dist))
                    if nbr.id == e_key:
                        return path
            curr_node.color = "BLACK"
        return path


    def shortest_path(self, algo, start, end):
        path = []
        if algo == 'bfs':
            path = self.bfs(start, end)
        return path

    def __str__(self):
        print("Graph exists")

def create_basic_graph():
    G1 = graph()

    for i in range(1, 101):
        vert = vertex('v' + str(i))
        G1.add_vertex(vert)

    for i in range(1, 95):
        for j in range(1, 7):
            G1.add_edge('v' + str(i), 'v' + str(i + j))

    for i in range(95, 100):
        for j in range(1, 7):
            if (i + j) <= 100:
                G1.add_edge('v' + str(i), 'v' + str(i + j))
    return G1


T = int(input())
for count in range(T):
    G = create_basic_graph()

    num_ladders = int(input())
    for each in range(num_ladders):
        line = input().split()
        start_ladder = 'v' + line[0]
        end_ladder = 'v' + line[1]
        G.replace_all_edges_to(start_ladder, end_ladder)
        G.drop_vertex(start_ladder)

    num_snakes = int(input())
    for each_ in range(num_snakes):
        line = input().split()
        start_snake = 'v' + line[0]
        end_snake = 'v' + line[1]
        G.replace_all_edges_to(start_snake, end_snake)
        G.drop_vertex(start_snake)

    path = (G.shortest_path('bfs', 'v1', 'v100'))
    if path[-1][0] == 'v100':
        print(path[-1][1])
    else:
        print('-1')













