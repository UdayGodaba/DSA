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
    
    def printDLL(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
    
    def appendEnd(self, value):     #O(1)
        new_node = Node(value)
        if self.head is None:    
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
            self.length += 1
    
    def popEnd(self):   #O(1)
        if self.length == 0:
            pass
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
    
    def prepend(self, value):   #O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def popFirst(self):     #O(1)
        if self.length == 0:
            pass
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.length -= 1

    def get(self, index):   # O(index)
        if index < 0 or index == self.length:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr
    
    def setVal(self, index, value): # O(index)
        curr = self.get(index)
        if curr:
            curr.value = value

    def insertVal(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.appendEnd(value)
            return
        curr = self.get(index - 1)
        if curr:
            new_node = Node(value)
            new_node.next = curr.next
            curr.next.prev = new_node
            new_node.prev = curr
            curr.next = new_node
            self.length += 1
        
    def removeVal(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.popFirst()
            return
        if index == self.length - 1:
            self.popEnd()
            return
        curr = self.get(index)
        if curr:
            curr.next.prev = curr.prev
            curr.prev.next = curr.next
            curr.prev = None
            curr.next = None
            self.length -= 1

my_DLL = DoubleLinkedList(1)
my_DLL.appendEnd(2)
my_DLL.appendEnd(3)
my_DLL.removeVal(4)
my_DLL.printDLL()