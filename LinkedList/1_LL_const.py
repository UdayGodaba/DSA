#To create a node we are using a class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#To create Linked List
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_linkedlist = LinkedList(4)
print(new_linkedlist.head.value)