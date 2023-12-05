# Find min value in given range for both arrays and return min value of the result
# Repeat the same after updating a value in either of the array

class SGTree:

    def __init__(self, n, arr):
        self.seg = [float("inf")] * (4*n + 1)
        self.arr = arr

    def build(self, idx, low, high):   # TC: O(4*N)
        # Base Case
        if low == high:
            self.seg[idx] = self.arr[low]
            return
        # Traverse
        mid = (low + high) // 2
        self.build(2*idx + 1, low, mid)
        self.build(2*idx + 2, mid + 1, high)
        # Update Value
        self.seg[idx] = min(self.seg[2*idx + 1], self.seg[2*idx + 2])
    
    def update(self, idx, low, high, pos, val):  # TC: O(logN)
        # Base Condition
        if low == high:
            self.seg[idx] = val
            return
        # Traverse
        mid = (low + high) // 2
        if pos <= mid:
            self.update(2*idx + 1, low, mid, pos, val)
        else:
            self.update(2*idx + 2, mid + 1, high, pos, val)
        # Update Value
        self.seg[idx] = min(self.seg[2*idx + 1], self.seg[2*idx + 2])

    def query(self, idx, low, high, l, r):   # TC: O(logN)
        # No overlap
        if r < low or high < l:
            return float("inf")
        # Complete Overlap
        if l <= low and high <= r:
            return self.seg[idx]
        # Partial Overlap
        mid = (low + high) // 2
        left = self.query(2*idx + 1, low, mid, l, r)
        right = self.query(2*idx + 2, mid + 1, high, l, r)
        return min(left, right)


arr1 = [1,0,3,2,4,2,1]
sg1 = SGTree(len(arr1), arr1)
sg1.build(0, 0, len(arr1)-1)

arr2 = [2,1,6,5,4,3,8]
sg2 = SGTree(len(arr2), arr2)
sg2.build(0, 0, len(arr2)-1)

first = sg1.query(0, 0, len(arr1) - 1, 2, 4)
second = sg2.query(0, 0, len(arr2) - 1, 2, 4)
if first < second:
    print("First Value: " , first)
else:
    print("Second Value: " , second)

sg2.update(0, 0, len(arr2)-1, 2, 1)

print("After Updating")
first = sg1.query(0, 0, len(arr1) - 1, 2, 4)
second = sg2.query(0, 0, len(arr2) - 1, 2, 4)
if first < second:
    print("First Value: " , first)
else:
    print("Second Value: " , second)