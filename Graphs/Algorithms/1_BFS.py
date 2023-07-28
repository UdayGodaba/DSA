my_graph = {
    1 : [2,6],
    2 : [1,3,4],
    3 : [2],
    4 : [2,5],
    5 : [4,8],
    6 : [1,7,9],
    7 : [6,8],
    8 : [5,7],
    9 : [6]
}

# Connected Components graph
my_graph = {
    1 : [2,6],
    2 : [1,3,4],      
    3 : [2],         
    4 : [2],
    5 : [8],
    6 : [1,7,9],
    7 : [6],
    8 : [5],
    9 : [6]
}

# Iterative approach
# Space Complexity : O(3V) --> O(V) and Time Complexity : O(V + V + 2*E) --> O(V + E)

def BFS(start, visited, my_graph, bfs):
    queue = [start]
    while len(queue) > 0:
        temp = queue.pop(0)
        if visited.get(temp, False):
            pass
        else:
            bfs.append(temp)
            visited[temp] = 1
            for neighbour in my_graph[temp]:
                if neighbour not in visited:
                    queue.append(neighbour)

visited = {}
bfs = []

# This loop is for connected components
for i in my_graph:
    if i not in visited:
        BFS(i, visited, my_graph, bfs)

print(bfs)