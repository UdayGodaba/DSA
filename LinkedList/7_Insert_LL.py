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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index > self.length:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, value, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index -1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linkedlist = LinkedList(1)
my_linkedlist.append(2)
my_linkedlist.append(3)
my_linkedlist.append(4)
my_linkedlist.printLinkedList()
print("After prepend")
my_linkedlist.prepend(0)
my_linkedlist.printLinkedList()
print("after insert")
my_linkedlist.insert(5,2)
my_linkedlist.printLinkedList()

# my_linkedlist = LinkedList(0)
# my_linkedlist.append(2)
# my_linkedlist.printLinkedList()
# my_linkedlist.insert(1,1)
# my_linkedlist.printLinkedList()
        
        
        