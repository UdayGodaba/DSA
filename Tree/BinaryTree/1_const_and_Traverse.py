class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def preOrder(self):
        res = []
        def preOrderHelper(curr, res):
            if curr is None:
                return
            res.append(curr.value)
            preOrderHelper(curr.left, res)
            preOrderHelper(curr.right, res)
        preOrderHelper(root, res)
        return res

    def inOrder(self):
        res = []
        def inOrderHelper(curr, res):
            if curr is None:
                return
            inOrderHelper(curr.left, res)
            res.append(curr.value)
            inOrderHelper(curr.right, res)
        inOrderHelper(root, res)
        return res

    def postOrder(self):
        res = []
        def postOrderHelper(curr, res):
            if curr is None:
                return
            postOrderHelper(curr.left, res)
            postOrderHelper(curr.right, res)
            res.append(curr.value)
        postOrderHelper(root, res)
        return res    
    
    def BFS(self):
        queue = [root]
        res = []
        while queue:
            temp = queue.pop(0)
            res.append(temp.value)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(root.preOrder())
print(root.inOrder())
print(root.postOrder())
print(root.BFS())