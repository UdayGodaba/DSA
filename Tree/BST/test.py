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

    def contains(self, value):

        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return print(f"{value} is found in BST")
        return print(f"{value} is not found in BST")

    def preOrder(self):

        results = []
        def preOrderHelper(current_node):

            results.append(current_node.value)
            if current_node.left is not None:
                preOrderHelper(current_node.left)
            if current_node.right is not None:
                preOrderHelper(current_node.right)

        preOrderHelper(self.root)
        return results

    def postOrder(self):

        results = []
        def postOrderHelper(current_node):
            
            if current_node.left is not None:
                postOrderHelper(current_node.left)
            if current_node.right is not None:
                postOrderHelper(current_node.right)
            results.append(current_node.value)
        
        postOrderHelper(self.root)
        return results
    
    def inOrder(self):

        results = []
        def inOrderHelper(current_node):
            
            if current_node.left is not None:
                inOrderHelper(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                inOrderHelper(current_node.right)
        
        inOrderHelper(self.root)
        return results

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.preOrder())
print(my_tree.postOrder())
print(my_tree.inOrder())