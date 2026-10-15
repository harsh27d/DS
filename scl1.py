class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head

    def insert_second_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        last = self.head
        while last.next != self.head:
            last = last.next

        if last == self.head:
            new_node.next = self.head
            self.head = new_node
            last.next = self.head
            return

        second_last = self.head
        while second_last.next.next != self.head:
            second_last = second_last.next

        new_node.next = last
        second_last.next = new_node

    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        prev = None

        if temp.data == value:
            if temp.next == self.head:
                self.head = None
                return

            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head
            return

        while temp.next != self.head and temp.data != value:
            prev = temp
            temp = temp.next

        if temp.data == value:
            prev.next = temp.next
        else:
            print("Value not found")

    def print(self):
        if self.head is None:
            print("Circular linked list is empty")
            return

        current = self.head
        values = []
        while True:
            values.append(str(current.data))
            current = current.next
            if current == self.head:
                break

        print(" -> ".join(values) + " -> " + str(self.head.data))


# Example usage
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(44)
cll.append(55)

cll.insert_second_last(99)

print("Circular linked list:")
cll.print()

cll.delete(55)
cll.delete(1)

print("Updated circular linked list:")
cll.print()
