n = 3
m = 4
queries = [[0, 1], [1, 2], [1, 1], [0, 2], [1, 3]]
def numberOfIslandII(n, m, queries):
    # Write your code here.
    count = 0
    mat = [[0 for _ in range(m)] for _ in range(n)]
    path = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    res = []

    for row, col in queries:
        if mat[row][col] == 0:
            mat[row][col] = 1
            temp = 0
            for r, c in path:
                nRow = row + r
                nCol = col + c
                if 0 <= nRow < n and 0 <= nCol < m and mat[nRow][nCol]:
                    temp += 1
            if temp:
                if count - (temp - 1) > 1:
                    count -= (temp - 1)
                else:
                    count = 1
            else:
                count += 1
            res.append(count)

    return res

x = numberOfIslandII(n, m, queries)
print(x)