# Sereja and Brackets
# Given a string containing '(' and ')' find length of correct brackets in the given range queries
# Correct Brackets insense total bracket i.e open + close
# 1-indexed queries

s = "())(())(())("
queries = [[1,1], [2,3], [1,2], [1,12], [8,12], [5,11], [2,10]]
n = len(s)

class SGTree:

    def __init__(self, n, s):
        self.seg = [[0, 0, 0] for _ in range(4*n + 1)]
        self.s = s
    
    def merge(self, lNode, rNode):
        open = lNode[0] + rNode[0] - min(lNode[0], rNode[1])
        close = lNode[1] + rNode[1] - min(lNode[0], rNode[1])
        full = lNode[2] + rNode[2] + min(lNode[0], rNode[1])
        return [open, close, full]

    def build(self, idx, low, high):
        # Base Condition
        if low == high:
            if s[low] == "(":
                self.seg[idx][0] = 1
            else:
                self.seg[idx][1] = 1
            return
        # Traverse
        mid = (low + high) // 2
        self.build(2*idx + 1, low, mid)
        self.build(2*idx + 2, mid + 1, high)
        # Update node
        self.seg[idx] = self.merge(self.seg[2*idx + 1], self.seg[2*idx + 2])

    def query(self, idx, low, high, l, r):
        # No Overlap
        if r < low or high < l:
            return [0, 0, 0]
        # Complete Overlap
        if l <= low and high <= r:
            return self.seg[idx]
        # Partial Overlap
        mid = (low + high) // 2
        left = self.query(2*idx + 1, low, mid, l, r)
        right = self.query(2*idx + 2, mid + 1, high, l, r)
        return self.merge(left, right)
    
sg1 = SGTree(n, s)
sg1.build(0, 0, n - 1)

for l, r in queries:
    x = sg1.query(0, 0, n - 1, l - 1, r - 1)
    print(x[2]*2)