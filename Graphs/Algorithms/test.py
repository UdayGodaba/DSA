# my_graph = {
#     1 : [2,6],
#     2 : [1,3,4],
#     3 : [2],
#     4 : [2,5],
#     5 : [4,8],
#     6 : [1,7,9],
#     7 : [6,8],
#     8 : [7,5],
#     9 : [6]
# }

# This is for connected component graph
# Space : O(2N) --> O(N)   Time : O(N + N + 2E)

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

def BFS(start, my_graph, visited):
    queue = [start]
    while len(queue) != 0:
        temp = queue.pop(0)
        if visited.get(temp, False):
            pass
        else:
            print(temp)
            visited[temp] = 1
            for val in my_graph[temp]:
                queue.append(val)

visited = {}

for i in my_graph:
    if visited.get(i, False):
        pass
    else:
        BFS(i, my_graph, visited)