adj = [ [[1,2]],
        [[3,1]],
        [[3,3]],
        [[]],
        [[0,3], [2,1]],
        [[4,1]],
        [[4,2], [5,3]]]

visited = {}
V = 7
stack = []

def DFS(n, adj, stack, visited):
    visited[n] = 1
    for arr in adj[n]:
        i = 0
        while i < len(arr):
            x = arr[0]
            if x not in visited:
                DFS(x, adj, stack, visited)
            i += 1
        stack.append(n)

for i in range(V):
    if i not in visited:
        DFS(i, adj, stack, visited)

print(stack)