class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.val))
            temp = temp.next
        print(" -> ".join(elements) if elements else "Empty List")

    def find_middle(self):
        if not self.head:
            print("List is empty!")
            return None

        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next

        mid_index = count // 2
        temp = self.head
        for _ in range(mid_index):
            temp = temp.next

        print(f"Middle node value: {temp.val}")
        return temp.val

    def delete_middle(self):
        if not self.head:
            print("List is empty!")
            return

        if not self.head.next:
            self.head = None
            return

        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next

        mid_index = count // 2
        temp = self.head
        for _ in range(mid_index - 1):
            temp = temp.next

        temp.next = temp.next.next

    def delfirst_last(self):
        if not self.head:
            print("List is empty!")
            return

        if not self.head.next or not self.head.next.next:
            self.head = None
            return

        self.head = self.head.next
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


if __name__ == "__main__":
    ll = SinglyLinkedList()
    for num in [10, 20, 30, 40, 50]:
        ll.append(num)

    print("Original List:")
    ll.display()
    print("\nFinding Middle:")
    ll.find_middle()
    print("\nDeleting Middle (30):")
    ll.delete_middle()
    ll.display()
    print("\nDeleting First (10) and Last (50):")
    ll.delfirst_last()
    ll.display()