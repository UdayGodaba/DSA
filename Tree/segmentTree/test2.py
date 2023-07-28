queries = [[1, 4], [3, 4], [1, 2], [1, 2]]
a = [1, 6, 3, 5]
n = len(a)
m = len(queries)

seg = [-1]*(4*n + 1)

def build(idx, low, high, flag):
    if low == high:
        seg[idx] = a[low]
        return
   
    mid = (low + high) // 2
    build(2*idx + 1, low, mid, not flag)
    build(2*idx + 2, mid+1, high, not flag)
    
    if flag:
        seg[idx] = seg[2*idx + 1] ^ seg[2*idx + 2]
    else:
        seg[idx] = seg[2*idx + 1] | seg[2*idx + 2]

def update(idx, low, high, pos, val, flag):
    if low == high:
        seg[idx] = val
        return
    
    mid = (low + high) // 2
    if pos <= mid:
        update(2*idx + 1, low, mid, pos, val, not flag)
    else:
        update(2*idx + 2, mid + 1, high, pos, val, not flag)
    
    if flag:
        seg[idx] = seg[2*idx + 1] ^ seg[2*idx + 2]
    else:
        seg[idx] = seg[2*idx + 1] | seg[2*idx + 2]


if n % 2 == 0:
    build(0, 0, n-1, 1)
else:
    build(0, 0, n-1, 0)

for pos, val in queries:
    if n % 2 == 0:
        update(0, 0, n-1, pos-1, val, 1)
    else:
        update(0, 0, n-1, pos-1, val, 0)
    
    print(seg[0])