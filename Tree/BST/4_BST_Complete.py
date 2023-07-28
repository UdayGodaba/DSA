class Node:
    
    def __init__(self, value):
    
        self.value = value
        self.left = None
        self.right = None 

class BinarySearchTree:
    
    def __init__(self):
    
        self.root = None

    def insert(self, value):

        new_node = Node(value)        
        if self.root is None:
            self.root = new_node
            return
        temp = self.root    
        while True:
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right
            else:
                return

    def Contains(self, value):

        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return print(f"{value} is Found")
        return print(f"{value} is not Found")

    def min_value(self):
        
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return print(f"{temp.value} is the min value in Tree")




my_tree = BinarySearchTree()
my_tree.insert(8)
my_tree.insert(3)
my_tree.insert(10)
my_tree.insert(1)
my_tree.insert(6)
my_tree.insert(4)
my_tree.insert(7)
my_tree.insert(14)
my_tree.insert(13)

# print(my_tree.root.left.right.left.value)
my_tree.Contains(14)
my_tree.min_value()
