# Singly linear linked list with append and insertion at a given position.

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insert(self, new_node, pos):
        if pos <= 1:
            new_node.next = self.head
            self.head = new_node
            return self.head

        temp = self.head
        index = 1
        while temp is not None and index < pos - 1:
            temp = temp.next
            index += 1

        if temp is None:
            raise IndexError("Position is out of range")

        new_node.next = temp.next
        temp.next = new_node
        return self.head

    def display(self):
        temp = self.head
        values = []
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(values) if values else "None")


if __name__ == "__main__":
    list1 = LinkedList()
    for value in [10, 20, 30, 40, 50]:
        list1.append(Node(value))
    print("Original List:")
    list1.display()
    list1.insert(Node(100), 1)
    print("\nAfter inserting 100 at position 1:")
    list1.display()
    list1.insert(Node(66), 4)
    print("\nAfter inserting 66 at position 4:")
    list1.display()

