# from copy import deepcopy
def orangesRotting(grid):
        
        m = len(grid)
        n = len(grid[0])
        # visited = deepcopy(grid)
        freshCount = 0
        tMax = 0
        queue = []

        # creating visited array and queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([[i, j], 0])
                    # visited[i][j] = 2
                elif grid[i][j] == 1:
                    # visited[i][j] = 0
                    freshCount += 1
        
        detRow = [-1, 0, 1, 0]
        detCol = [0, 1, 0, -1]
        rottenCount = 0
        
        # Traversing using BFS so that it rottens neighbours uniformly and in min Time
        while len(queue) > 0:
            r = queue[0][0][0]
            c = queue[0][0][1]
            t = queue[0][1]
            tMax = max(tMax, t)
            queue.pop(0)
            for i in range(4):
                newRow = r + detRow[i]
                newCol = c + detCol[i]
                if (newRow >= 0 and newRow < m and newCol >= 0 and newCol < n and grid[newRow][newCol] != 2 and grid[newRow][newCol] == 1):
                    queue.append([[newRow, newCol], t + 1])
                    # visited[newRow][newCol] = 2
                    grid[newRow][newCol] = 2
                    rottenCount += 1
        
        
        if rottenCount != freshCount:
            return -1
        else:
            return tMax

grid = [[0,2]]
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))