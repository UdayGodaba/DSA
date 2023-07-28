class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printDoubleLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_dll = DoubleLinkedList(1)
my_dll.printDoubleLinkedList()