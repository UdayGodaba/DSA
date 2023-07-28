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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def popfirst(self):
        if self.length == 0:
           return None
        if self.length == 1:
             self.head = None
             self.tail = None
        else:
            temp = self.head 
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1

my_DLL = DoubleLinkedList(1)
my_DLL.prepend(0)
my_DLL.print_list()
print("After popfirst")
my_DLL.popfirst()
my_DLL.print_list()
print("After popfirst")
my_DLL.popfirst()
my_DLL.print_list() 
