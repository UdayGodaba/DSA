my_graph = {
            0 : [1],
            1 : [0,2,4],
            2 : [1,3],
            3 : [2,4],
            4 : [4,3]
            }

# my_graph = {
#             0 : [2,3],
#             1 : [3],
#             2 : [0, 3],
#             3 : [0,1,2]
#             }

# print(my_graph)
        
def DFS(start, my_graph, visited):
    
    stack = [[start, -1]]

    while len(stack) > 0:
        temp = stack.pop()
        if visited.get(temp[0], False):
            if visited[temp[0]] != temp[1]:
                return 1
            else:
                pass
        else:
            # print(temp)
            visited[temp[0]] = temp[1]
            for val in my_graph[temp[0]]:
                if val not in visited:
                    stack.append([val, temp[0]])
visited = {}
flag = 0   

for i in my_graph:
    if i not in visited:
        if DFS(i, my_graph, visited):
            flag = 1

if flag == 1:
    print("There is cycle")
else:
    print("No Cycle")