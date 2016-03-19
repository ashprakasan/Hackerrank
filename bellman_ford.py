INF = 999999  # Infinity


# function to get incoming edges to v
def get_inc_edges(v):
    inc = []
    for i in range(V + 1):
        if G[i][v] != INF and G[i][v] != 0:
            inc.append(i)
    return inc


V = int(input())
E = int(input())
G = [[INF] * (V + 1) for a in range(V + 1)]  # representing the graph as an adj matrix
for ind in range(V + 1):
    G[ind][ind] = 0
for count in range(E):
    inp = input().split()
    v1 = int(inp[0])
    v2 = int(inp[1])
    wt = int(inp[2])
    G[v1][v2] = wt
s = int(input())  # start node
dist_prev = [INF] * (V + 1)
dist_prev[s] = 0
k = 0
while k < V - 1:
    dist_curr = [INF] * (V + 1)
    for v in range(1, V + 1):
        if v != s:
            inc = get_inc_edges(v)
            for vert in inc:
                dist_curr[v] = min(dist_prev[vert] + G[vert][v], dist_prev[v], dist_curr[v])
        else:
            dist_curr[v] = 0
    for i in range(len(dist_curr)):
        dist_prev[i] = dist_curr[i]
    print(dist_curr, k)
    k += 1
print(" The shortest distances from start node to all vertices:")
print(dist_curr[1:])
