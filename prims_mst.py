__author__ = 'aiswarya'
import heapq


def prims(G, start):
    N = len(G) - 1
    mstSet = []
    weight = [INF] * (N + 1)
    weight[start] = 0
    weight[start] = 0
    wt = (0, start)
    heap_wt = []
    mstSet.append(start)
    heapq.heappush(heap_wt, wt)
    curr = heapq.heappop(heap_wt)[1]
    while len(mstSet) < N:
        adj = G[curr]
        for each in adj:
            if each not in mstSet:
                if weight[each] > G[curr][each]:
                    weight[each] = G[curr][each]
                    heapq.heappush(heap_wt, (weight[each], each))
            curr = heapq.heappop(heap_wt)[1]
            mstSet.append(curr)
    tot_weight = 0
    for i in range(1, len(weight)):
        tot_weight = tot_weight + weight[i]
    return tot_weight


line = input().split()
INF = 100000000000000
N = int(line[0])
M = int(line[1])
G = [None] * (N + 1)
for each in range(M):
    line = input().split()
    v1 = int(line[0])
    v2 = int(line[1])
    weight = int(line[2])
    if G[v1] == None:
        G[v1] = []
    G[v1].append(v2)
    if G[v2] == None:
        G[v2] = []
    G[v2].append(v1)
start = int(input())
tot_weight = prims(G, start)
print(tot_weight)


