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

    def append(self, value):
        new_node = Node(value)
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:    # for 1 node case
            self.head = None
            self.tail = None
        return temp


my_LinkedList = LinkedList(1)
my_LinkedList.append(2)
my_LinkedList.append(3)
my_LinkedList.append(4)
my_LinkedList.append(5)
my_LinkedList.printLinkedList() 
print("Now using POP : \n")
my_LinkedList.pop()
my_LinkedList.printLinkedList()
print("Now using POP : \n")
my_LinkedList.pop()
my_LinkedList.printLinkedList()

        
