#WAP to print node values in reverse order in Dobly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def print_reverse(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        print("List elements in reverse order:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()
list1 = LinkedList()
list1.append(Node(1))
list1.append(Node(2))
list1.append(Node(3))
list1.print_reverse()

