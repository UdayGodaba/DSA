s = "())(())(())("
queries = [[1,1], [2,3], [1,2], [1,12], [8,12], [5,11], [2,10]]
n = len(s)
# In segment array arr[i][0] = open, arr[i][1] = close, arr[i][2] = full
seg = [[0, 0, 0] for _ in range(4*n+1)]

def merge(lNode, rNode):
    ans = [0, 0, 0]
    ans[0] = lNode[0] + rNode[0] - min(lNode[0], rNode[1])
    ans[1] = lNode[1] + rNode[1] - min(lNode[0], rNode[1])
    ans[2] = lNode[2] + rNode[2] + min(lNode[0], rNode[1])
    return ans

def build(idx, low, high):
    
    if low == high:
        if s[low] == "(":
            seg[idx][0] = 1
        else:
            seg[idx][1] = 1
        return
    
    mid = (low + high) // 2
    build(2*idx + 1, low, mid)
    build(2*idx + 2, mid+1, high)
    
    seg[idx] = merge(seg[2*idx + 1], seg[2*idx + 2])

def query(idx, low, high, l, r):
    # no overlap
    if r < low or high < l:
        return [0, 0, 0]
    # complete overlap
    if l <= low and high <= r:
        return seg[idx]
    # partial overlap
    mid = (low + high) // 2
    left = query(2*idx + 1, low, mid, l, r)
    right = query(2*idx + 2, mid + 1, high, l, r)
    return merge(left, right)

build(0, 0, n-1)
for l, r in queries:
    x = query(0, 0, n-1, l-1, r-1)
    print(x[2]*2)