
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node
    def insert(self, new_node, pos):
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            p = 1
            while p < pos - 1 and temp:
                temp = temp.next
                p += 1
            if temp is None:
                print("Invalid position")
                return
            new_node.next = temp.next
            new_node.prev = temp
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node
    def print(self):
        temp = self.head
        print("List elements:", end=" ")

        while temp.next:
            #print(temp.data, end=" ")
            temp = temp.next
        print(temp.data, end=" ")
        while temp:
                print(temp.data, end=" ")
                temp = temp.prev
        print()


list1 = LinkedList()
list1.append(Node(1))
list1.append(Node(2))
list1.append(Node(3))
list1.print()
list1.insert(Node(4), 2)
list1.print()
