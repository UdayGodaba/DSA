class Node:
    def __init__(self, value):     # we create seperate class for node as it is reused everytime
        self.value = value         # Node contains value and next address by default none if new node
        self.next = None

class LinkedList:
    def __init__(self, value):     # LL initalization
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printLinkedList(self):     # printing linkedlist
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):              # Append adds new node at end
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):                  # pop method removes node from end of LL
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
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):           # adds node at starting
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):                # removes node at starting
        if self.length == 0:
            return None
        temp = self.head 
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def get(self, index):                           # get method gets the node at specified index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):               # set value method sets value specified at specified index
        temp = self.get(index)
        if temp:
            temp.value = value
            return True 
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index-1)
        if temp:
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        pre = self.get(index -1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.prepend(0)
my_linked_list.printLinkedList()
print("After set new value in index specified")
my_linked_list.set_value(3,4)
my_linked_list.printLinkedList()
print("Now inserting 3 in between")
my_linked_list.insert(3,3)
my_linked_list.printLinkedList()
print("inserting 5 at end")
my_linked_list.insert(5,5)
my_linked_list.printLinkedList()
print("Removing an item using remove")
my_linked_list.remove(3)
my_linked_list.printLinkedList()





