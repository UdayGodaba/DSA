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
            self.tail = self.tail.next
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
    
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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, value, index):
        temp = self.get(index)
        if (temp):
            temp.value = value
        else:
            return None

    def insert(self, value, index):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return None 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index-1)
        if (temp):
            after = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next = new_node
            after.prev = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None 
        if index == 0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)
        if (temp):
            after = temp.next
            before = temp.prev
            before.next = after
            after.prev = before
            temp.next = None
            temp.prev = None
        self.length -= 1



my_dll = DoubleLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
my_dll.insert(0,0)
my_dll.pop()
my_dll.popfirst()
my_dll.remove(2)
my_dll.print_list()
