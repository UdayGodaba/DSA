class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.root = new_node

    def __init__(self):
        self.root = None               # In this we are creating a empty root node

my_BST = BinarySearchTree()
print(my_BST.root)