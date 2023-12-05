# Lazy Propagation
# Used for cases where there is range of values updated

a = [7, 2, 5, 9, 1, 3]
n = len(a)

class SGTree:

    def __init__(self, n, arr):
        self.seg = [0]*(4*n)
        self.lazy = [0]*(4*n)
        self.arr = arr

    def printSL(self):
        return print(self.seg, self.lazy)
    
    def build(self, idx, low, high):
        # Base Condition
        if low == high:
            self.seg[idx] = self.arr[low]
            return
        # Traverse
        mid = (low + high) // 2
        self.build(2*idx + 1, low, mid)
        self.build(2*idx + 2, mid + 1, high)
        # Update
        self.seg[idx] = self.seg[2*idx + 1] + self.seg[2*idx + 2]

    def update(self, idx, low, high, l, r, val):
        # Incase the lazy node is not Zero
        if self.lazy[idx] != 0:
            self.seg[idx] += (high - low + 1) * self.lazy[idx]
            # If not leaf node
            if low != high:
                self.lazy[2*idx + 1] += self.lazy[idx]
                self.lazy[2*idx + 2] += self.lazy[idx]
            # As the lazy value is propagated to children now we empty it for the parent node
            self.lazy[idx] = 0
        
        # No overlap just return
        if high < l or low > r:
            return
        # Complete overlap return updated value
        if l <= low and high <= r:
            self.seg[idx] += (high - low + 1) * val
            # Not a leaf then we need to propagate val into children
            if low != high:
                self.lazy[2*idx + 1] += val
                self.lazy[2*idx + 2] += val
            return
        # Partial Overlap
        mid = (low + high) // 2
        self.update(2*idx + 1, low, mid, l, r, val)
        self.update(2*idx + 2, mid + 1, high, l, r, val)
        self.seg[idx] = self.seg[2*idx + 1] + self.seg[2*idx + 2]

    def query(self, idx, low, high, l, r):
        # Incase the lazy node is not Zero
        if self.lazy[idx] != 0:
            self.seg[idx] += (high - low + 1) * self.lazy[idx]
            # If not leaf node
            if low != high:
                self.lazy[2*idx + 1] += self.lazy[idx]
                self.lazy[2*idx + 2] += self.lazy[idx]
            # As the lazy value is propagated to children now we empty it for the parent node
            self.lazy[idx] = 0

        # No Overlap
        if high < l or low > r:
            return 0
        # Complete overlap return updated value
        if l <= low and high <= r:
            return self.seg[idx]
        # Partial Overlap
        mid = (low + high) // 2
        left = self.query(2*idx + 1, low, mid, l, r)
        right = self.query(2*idx + 2, mid + 1, high, l, r)
        return left + right

sg1 = SGTree(n, a)
sg1.build(0, 0, n - 1)
sg1.printSL()
print(sg1.query(0, 0, n - 1, 2, 4))
sg1.update(0, 0, n - 1, 2, 4, 2)
sg1.printSL()