from re import M


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

    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def setvalue(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return None

my_linkedlist = LinkedList(1)
my_linkedlist.append(2)
my_linkedlist.append(3)
my_linkedlist.append(4)
my_linkedlist.printLinkedList()
print("getting value at index")
my_linkedlist.get(1)
print("changing value at index")
my_linkedlist.setvalue(5,1)
my_linkedlist.printLinkedList()
