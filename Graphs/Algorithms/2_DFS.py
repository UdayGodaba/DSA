my_graph = {
    1 : [2,3],
    2 : [1,5,6],
    3 : [1,4,7],
    4 : [3,8],
    5 : [2],
    6 : [2],
    7 : [3,8],
    8 : [4,7]
}

# Connected Components graph
my_graph = {
    1 : [2,3],
    2 : [1,5,6],
    3 : [1],
    4 : [8],
    5 : [2],
    6 : [2],
    7 : [8],
    8 : [4,7]
}

# Iterative Method
# Space Complexity : O(3V) --> O(V)  and Time Complexity : O(V + V + 2*E) --> O(V + E)

def DFS(start, visited, my_graph, dfs):
    stack = [start]
    while len(stack) > 0:
        temp = stack.pop()
        if visited.get(temp, False):
            pass
        else:
            dfs.append(temp)
            visited[temp] = 1
            for neighbour in my_graph[temp]:
                if neighbour not in visited:
                    stack.append(neighbour)

dfs = []
visited = {}

for i in my_graph:
    if i not in visited:
        DFS(i, visited, my_graph, dfs)
print(dfs)
        
# Recursive Method
# Space Complexity : O(V) and Time Complexity : O(V + V + 2*E) --> O(V + E) for Undirected if directed 2*E --> E

dfs = []
visited = {}

def DFS(temp, visited, dfs, my_graph):
    dfs.append(temp)
    visited[temp] = 1
    for neighbour in my_graph[temp]:
        if neighbour not in visited:
            DFS(neighbour, visited, dfs, my_graph)

for i in my_graph:
    if i not in visited:
        DFS(i, visited, dfs, my_graph)
print(dfs)