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
        while temp:
            print(temp.value)
            temp = temp.next
    
    def appendNode(self, value):           #O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def popNode(self):                     #O(n)
        if self.head is None:
            return
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None
        self.tail = pre
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
    
    def prependNode(self, value):          #O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def popFirstNode(self):               #O(1)
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None


    def getNode(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def setValueNode(self, value, index):
        temp = self.getNode(index)
        if temp:
            temp.value = value

    def insertNode(self, value, index):
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.prependNode(value)
            return
        if index == self.length:
            self.appendNode(value)
            return
        temp = self.getNode(index - 1)
        if temp:
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def removeNode(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.popFirstNode()
            return
        if index == self.length - 1:
            self.popNode()
            return
        pre = self.getNode(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1 
    
    def reverseLL(self):
        if self.head is None or self.length == 1:
            return
        curr = self.head
        pre = None
        post = curr.next
        self.head , self.tail = self.tail, self.head
        while post:
            curr.next = pre
            pre = curr
            curr = post
            post = post.next
        curr.next = pre

my_Linked_List = LinkedList(1)
my_Linked_List.appendNode(2)
my_Linked_List.appendNode(3)
my_Linked_List.appendNode(4)
my_Linked_List.appendNode(5)
print("Before Reversing")
my_Linked_List.printLinkedList()
print("After Reversing")
my_Linked_List.reverseLL()
my_Linked_List.printLinkedList()