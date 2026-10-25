class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def concatenate(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        if not other_list.head:
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = other_list.head

    def display(self):
        curr = self.head
        values = []
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(values) if values else "None")


if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)

    list2 = LinkedList()
    list2.append(4)
    list2.append(5)
    list2.append(6)

    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()
    list1.concatenate(list2)
    print("\nAfter Concatenation:")
    list1.display()
