class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def printLL(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
    
    def appendEnd(self, value):        #O(1)
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length = 1
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
            self.length += 1
    
    def popLast(self):                  #O(N)
        if self.length == 0:
            pass
        else:
            curr = self.head
            pre = curr
            while curr.next:
                pre = curr
                curr = curr.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
    
    def prepend(self, value):       #O(1)
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length = 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
        
    def popFirst(self):         #O(1)
        if self.length == 0:
            pass
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
    
    def get(self, index):       #O(index)
        if index >= self.length or index < 0:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next        
        return curr
    
    def setVal(self, index, value):     #O(index)
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
            newNode = Node(value)
            newNode.next = curr.next
            curr.next = newNode
            self.length += 1
    
    def removeVal(self, index):
        if index == 0:
            self.popFirst()
            return
        if index == self.length - 1:
            self.popLast()
            return
        curr = self.get(index-1)
        if curr:
            temp = curr.next
            curr.next = temp.next
            temp.next = None
            self.length -= 1

my_LL = LinkedList(1)
my_LL.appendEnd(4)
my_LL.appendEnd(3)
# my_LL.setVal(1, 2)
my_LL.insertVal(3, 4)
my_LL.insertVal(1, 2)
my_LL.insertVal(-1, 2)
my_LL.removeVal(2)
my_LL.removeVal(3)
my_LL.removeVal(0)
my_LL.printLL()