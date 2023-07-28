my_graph = {
            0 : [],
            1 : [],
            2 : [3],
            3 : [1],
            4 : [0,1],
            5 : [0,2]
            }

# Time Complexity : O(2V + E) --> O(V + E)  and Space : O(3V) --> O(V)

def DFS(n, my_graph, visited, stack):
    visited[n] = 1
    for val in my_graph[n]:
        if val not in visited:
            DFS(val, my_graph, visited, stack)
    stack.append(n)

stack = []
visited = {}

for i in my_graph:
    if i not in visited:
        DFS(i, my_graph, visited, stack)

print(stack[::-1])