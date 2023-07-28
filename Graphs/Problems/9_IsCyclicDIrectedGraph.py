# my_graph = {
#             0 : [1],
#             1 : [2],
#             2 : [3,4],
#             3 : [4],
#             4 : [],
#             5 : [2,6],
#             6 : [7],
#             7 : [5]
#             }

my_graph = {
            0 : [1],
            1 : [2],
            2 : [3],
            3 : [3]
            }

visited = {}
path = []


def DFS(temp, visited, my_graph, path):
    visited[temp] = 1
    for val in my_graph[temp]:
        if val not in visited:
            if DFS(val, visited, my_graph, path + [val]):
                return True
        elif val in path:
            print("True")
            return 1

for i in my_graph:
    if i not in visited:
        if DFS(i, visited, my_graph, path + [i]):
            print("Done")