E = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
S = 2
V = 3

# E = [[0,1,2],[1,2,-1],[2,0,-2]]
# S = 0
# V = 3

def BellmanFord(V, edges, S):
    # Forming distance array
    dist = []
    for _ in range(V):
        dist.append(1e8)
    dist[S] = 0
    # Relaxing edges for N-1 iterations
    for _ in range(V - 1):
        for a in edges:
            u = a[0]
            v = a[1]
            wt = a[2]
            if dist[u] != 1e8 and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
    # Relaxing edges for Nth iteration to check if cycle exists
    # Cycle exists if dist values reduces after N-1 iteration so we do Nth iteration
    for a in edges:
            u = a[0]
            v = a[1]
            wt = a[2]
            if dist[u] != 1e8 and dist[u] + wt < dist[v]:
                return -1
    return dist

print(BellmanFord(V, E, S))