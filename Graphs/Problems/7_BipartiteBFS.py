def BFS(start, color, my_graph):
    queue = [[start, 0]]
    while len(queue) > 0:
        temp = queue.pop(0)
        if color.get(temp[0], False):
            if color[temp[0]] != temp[1]:
                return True
        else:
            color[temp[0]] = temp[1]
            if temp[1] == 1:
                c = 0
            else:
                c = 1
            for val in my_graph[temp[0]]:
                queue.append([val, c])
    return False

def isBipartite(my_graph, color):
    for i in my_graph:
        if i not in color:
            if BFS(i, color, my_graph):
                return False
    return True

color = {}
# my_graph = {
#             0 : [2, 3],
#             1 : [3],
#             2 : [0, 3],
#             3 : [0, 1, 2]
#             }
my_graph = {
            0 : [1],
            1 : [0,2,4],
            2 : [1,3],
            3 : [2,4],
            4 : [1,3]
            }

print(isBipartite(my_graph, color))