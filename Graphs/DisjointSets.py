class DisjointSet:

    def __init__ (self, n):
        self.parent = [0] * (n + 1)
        self.size = [1] * (n + 1)
        for i in range(n + 1):
            self.parent[i] = i
    
    def findUParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] >= self.size[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

ds1 = DisjointSet(7)
print("same") if ds1.findUParent(1) == ds1.findUParent(2) else print("not same")
ds1.unionBySize(1, 2)
print("same") if ds1.findUParent(1) == ds1.findUParent(2) else print("not same")
ds1.unionBySize(2, 3)
ds1.unionBySize(4, 5)
ds1.unionBySize(6, 7)
ds1.unionBySize(5, 6)
print("same") if ds1.findUParent(3) == ds1.findUParent(7) else print("not same")
ds1.unionBySize(3, 7)
print("same") if ds1.findUParent(3) == ds1.findUParent(7) else print("not same")