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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None 
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
        
my_DLL = DoubleLinkedList(1)
my_DLL.append(2)
my_DLL.append(3)
my_DLL.print_list()
print("After pop")
my_DLL.pop()
my_DLL.print_list()
print("After pop")
my_DLL.pop()
my_DLL.print_list()
print("After pop")
my_DLL.pop()
my_DLL.print_list()