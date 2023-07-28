my_graph = {
    'a' : ['c', 'b'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

print("Printing DFS")
stack = ['a']
while len(stack) > 0:
    temp = stack.pop()
    print(temp)
    for val in my_graph[temp]:
        stack.append(val)

print("Printing BFS")
queue = ['a']
while len(queue) > 0:
    temp = queue.pop(0)
    print(temp)
    for val in my_graph[temp]:
        queue.append(val)