class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):            # to append at end of linkedlist
        new_node = Node(value)
        if self.head is None:          # to check if linkedlist exists previously else if will be new and have h and t
            self.head = new_node       # if statement can also be written as self.length == 0
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1    

my_LinkedList = LinkedList(1)           #created an object
my_LinkedList.append(2)                 # Always call an method using class object not through class it will rise an error missing self
my_LinkedList.printLinkedList()


