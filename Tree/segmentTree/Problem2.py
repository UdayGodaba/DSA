# Xenia and Bit Operatins
# Given a arr 'a' contains 2^n values 1-indexed first perform OR next XOR so on alternate till you end up with one value and return the value
# You will be given queries [pos, val] update and return that top value

queries = [[1, 4], [3, 4], [1, 2], [1, 2]]
a = [1, 6, 3, 5]
# a = [1, 2, 3, 4]
# a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
m = len(queries)

class SGTree:

    def __init__(self, n, arr):
        self.seg = [-1] * (4*n + 1)
        self.arr = arr
    
    def pSeg(self):
        return print(self.seg[0])
    
    def build(self, idx, low, high, flag):
        # Base Condition
        if low == high:
            self.seg[idx] = self.arr[low]
            return
        # Traverse
        mid = (low + high) // 2
        self.build(2*idx + 1, low, mid, not flag)
        self.build(2*idx + 2, mid + 1, high, not flag)
        # Updating segment value
        if flag:
            self.seg[idx] = self.seg[2*idx + 1] ^ self.seg[2*idx + 2]
        else:
            self.seg[idx] = self.seg[2*idx + 1] | self.seg[2*idx + 2]
    
    def update(self, idx, low, high, pos, val, flag):
        # Base Condition
        if low == high:
            self.seg[idx] = val
            return
        # Traverse
        mid = (low + high) // 2
        if pos <= mid:
            self.update(2*idx + 1, low, mid, pos, val, not flag)
        else:
            self.update(2*idx + 2, mid + 1, high, pos, val, not flag)
        # Updating segment Value
        if flag:
            self.seg[idx] = self.seg[2*idx + 1] ^ self.seg[2*idx + 2]
        else:
            self.seg[idx] = self.seg[2*idx + 1] | self.seg[2*idx + 2]

sg1 = SGTree(len(a), a)
if n % 2 == 0:
    sg1.build(0, 0, len(a) - 1, 1)
else:
    sg1.build(0, 0, len(a) - 1, 0)
sg1.pSeg()

for pos, val in queries:
    if n % 2 == 0:
        sg1.update(0, 0, len(a) - 1, pos - 1, val, 1)
    else:
        sg1.update(0, 0, len(a) - 1, pos - 1, val, 0)
    sg1.pSeg()