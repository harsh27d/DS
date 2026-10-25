# Traversing and inserting in a singly linked list.

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        temp = self.head
        values = []
        while temp:
            values.append(str(temp.data))
            temp = temp.next
        return " -> ".join(values) if values else "None"

    def insertion(self, pos, val):
        new_node = Node(val)
        if pos <= 0:
            new_node.next = self.head
            self.head = new_node
            return self.head

        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                raise IndexError("Position is out of range")
            temp = temp.next

        if temp is None:
            raise IndexError("Position is out of range")

        new_node.next = temp.next
        temp.next = new_node
        return self.head


if __name__ == "__main__":
    ll = LinkedList()
    for value in [10, 20, 30, 40]:
        ll.append = lambda val=value, head=ll.head: None
    
    ll.head = Node(10)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)
    print("Original list:", ll.traversal())
    ll.insertion(1, 25)
    print("After insertion:", ll.traversal())
