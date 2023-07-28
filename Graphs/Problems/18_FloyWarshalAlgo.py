from copy import deepcopy
matrix = [[0,25], [-1,0]]
matrix = [[0,1,43],[1,0,6],[-1,-1,0]]
n = len(matrix)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == -1:
            matrix[i][j] = float('inf')
for via in range(n):
    pre = deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(pre[i][j], pre[i][via] + pre[via][j])
for i in range(n):
    for j in range(n):
        if matrix[i][j] == float('inf'):
            matrix[i][j] = -1

print(matrix)