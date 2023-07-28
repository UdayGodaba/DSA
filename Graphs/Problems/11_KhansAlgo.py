my_graph = {
            0 : [],
            1 : [],
            2 : [3],
            3 : [1],
            4 : [0,1],
            5 : [0,2]
            }
# my_graph = {
#             0 : [],
#             1 : [3],
#             2 : [3],
#             3 : [],
#             4 : [0,1],
#             5 : [0,2]
#             }

# Time Complexity : O(V + E) and Space Complexity : O(V)

inDegree = [0]*len(my_graph)
res = []
queue = []

# T : O(V + E)
for i in my_graph:
    for j in my_graph[i]:
        inDegree[j] += 1

#  T : O(V) S : O(V)
for i in range(len(inDegree)):
    if inDegree[i] == 0:
        queue.append(i)

#  T : O(V + E)  S : O(V)
while len(queue) > 0:
    temp = queue.pop(0)
    res.append(temp)
    for val in my_graph[temp]:
        inDegree[val] -= 1
        if inDegree[val] == 0:
            queue.append(val)

print(res)