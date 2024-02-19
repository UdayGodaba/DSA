class MaxHeap:
    def __init__(self):
        self.heap = []

    def left_child_idx(self, idx):
        return 2*idx + 1
    
    def right_child_idx(self, idx):
        return 2*idx + 2
    
    def parent_idx(self, idx):
        return (idx - 1) // 2
    
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1] 
    
    def insert(self, val):
        self.heap.append(val)
        curr = len(self.heap) - 1
        while curr > 0 and self.heap[curr] > self.heap[self.parent_idx(curr)]:
            self.swap(curr, self.parent_idx(curr))
            curr = self.parent_idx(curr)
    
    def sink_down(self, idx):
        max_idx = idx
        while True:
            left_idx = self.left_child_idx(idx)
            right_idx = self.right_child_idx(idx)

            if (left_idx < len(self.heap)) and (self.heap[left_idx] > self.heap[max_idx]):
                max_idx = left_idx

            if (right_idx < len(self.heap)) and (self.heap[right_idx] > self.heap[max_idx]):
                max_idx = right_idx
            
            if max_idx != idx:
                self.swap(idx, max_idx)
                idx = max_idx
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        maxVal = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)
        return maxVal
    
    def display(self):
        print(self.heap)

heap = MaxHeap()

heap.insert(99)
heap.display()

heap.insert(68)
heap.display()

heap.insert(72)
heap.display()

heap.insert(55)
heap.display()

heap.insert(75)
heap.display()

heap.insert(100)
heap.display()

heap.remove()
heap.display()
heap.remove()
heap.display()
heap.remove()
heap.display()