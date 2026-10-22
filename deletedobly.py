# Doubly linear linked list.

class Node:
    def __init__(self, value):
        self.data = value
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
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert(self, new_node, pos):
        if pos <= 1:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
            return

        temp = self.head
        p = 1
        while temp is not None and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            raise IndexError("Invalid position")

        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node

    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp is not None and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Node not found")
            return

        if temp.prev is None:
            self.head = temp.next
        else:
            temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        temp.next = None
        temp.prev = None

    def display(self):
        temp = self.head
        values = []
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(values) if values else "None")

    def display_reverse(self):
        temp = self.head
        if temp is None:
            print("None")
            return
        while temp.next is not None:
            temp = temp.next
        values = []
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.prev
        print(" <- ".join(values) if values else "None")

    def count_occurrences(self, value):
        count = 0
        temp = self.head
        while temp is not None:
            if temp.data == value:
                count += 1
            temp = temp.next
        return count

    def swap_first_last(self):
        if self.head is None or self.head.next is None:
            return
        last = self.head
        while last.next is not None:
            last = last.next
        self.head.data, last.data = last.data, self.head.data

    def swap(self):
        self.swap_first_last()


if __name__ == "__main__":
    list1 = LinkedList()
    for value in [10, 20, 30, 40]:
        list1.append(Node(value))

    print("Original List:")
    list1.display()
    print("\nList in reverse:")
    list1.display_reverse()
    list1.delete(20)
    print("\nAfter deleting 20:")
    list1.display()
    print("\nCount of 10:", list1.count_occurrences(10))
    list1.swap_first_last()
    print("\nAfter swapping first and last nodes:")
    list1.display()