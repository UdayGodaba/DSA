my_graph = {
            0 : [1],
            1 : [0,2,4],
            2 : [1,3],
            3 : [2,4],
            4 : [1,3]
            }


# print(my_graph)
        
def BFS(start, my_graph, visited):
    
    queue = [[start, -1]]

    while len(queue) > 0:
        temp = queue.pop(0)
        if visited.get(temp[0], False):
            if visited[temp[0]] != temp[1]:
                return 1
            else:
                pass
        else:
            print(temp)
            visited[temp[0]] = temp[1]
            for val in my_graph[temp[0]]:
                if val not in visited:
                    queue.append([val, temp[0]])
visited = {}
flag = 0   

for i in my_graph:
    if i not in visited:
        if BFS(i, my_graph, visited):
            flag = 1

if flag == 1:
    print("There is cycle")
else:
    print("No Cycle")