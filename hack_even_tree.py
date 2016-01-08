__author__ = 'aiswarya'

subtree = {}
num_break_edge = 0


def get_subtree(G, v):
    global subtree
    if G[v] == None:
        subtree[v] = 1
        return 1
    children = G[v]
    node_count = 1
    for each in children:
        node_count = node_count + get_subtree(G, each)
    subtree[v] = node_count
    return node_count


def dfs_count_break_edge(G, v):
    global num_break_edge
    if subtree[v] == 1:
        return
    adj = G[v]
    for each in adj:
        if subtree[each] % 2 == 0:
            num_break_edge += 1
        dfs_count_break_edge(G, each)


line = input().split()
N = int(line[0])
M = int(line[1])
G = [None] * (N + 1)
root = 1
for each in range(M):
    line = input().split()
    v2 = int(line[0])
    v1 = int(line[1])
    if G[v1] == None:
        G[v1] = []
    G[v1].append(v2)
    if each == 0:
        root = v1
get_subtree(G, root)
dfs_count_break_edge(G, root)
print(num_break_edge)


