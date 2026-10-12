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
        # If the first list is empty, point its head to the other list's head
        if not self.head:
            self.head = other_list.head
            return

        # If the second list is empty, nothing to attach
        if not other_list.head:
            return

        # Traverse to the end of the first list and link to the second
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = other_list.head

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


# --- Test Run ---
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

# Concatenate list2 onto list1
list1.concatenate(list2)

print("\nAfter Concatenation:")
list1.display()
