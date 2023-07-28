from copy import deepcopy

grid = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]

# grid = [[1, 1, 0, 1, 1],
#             [1, 0, 0, 0, 0],
#             [0, 0, 0, 0, 1],
#             [1, 1, 0, 1, 1]]
visited = deepcopy(grid)
        
n = len(grid)
m = len(grid[0])
visited = deepcopy(grid)


def BFS(position, visited, res):
    
    queue = [position]
    detRow = [-1, 0, 1, 0]
    detCol = [0, 1, 0, -1]
    temp = []
    while len(queue) > 0:
        r = queue[0][0]
        c = queue[0][1]
        queue.pop(0)
        temp.append([r, c])
        for i in range(4):
            nRow = r + detRow[i]
            nCol = c + detCol[i]
            if (nRow >= 0 and nRow < n and nCol >= 0 and nCol < m and visited[nRow][nCol] != 2 and grid[nRow][nCol] == 1):
                visited[nRow][nCol] = 2
                queue.append([nRow, nCol])
    sub = deepcopy(temp[0])
    for i in range(len(temp)):
        for j in range(2):
            temp[i][j] -= sub[j]
    if temp not in res:
        res.append(temp)

res = []
for i in range(n):
    for j in range(m):
        if visited[i][j] != 2 and grid[i][j] == 1:
            BFS([i, j], visited, res)
        
# print(grid)
# print(visited)
print(len(res))