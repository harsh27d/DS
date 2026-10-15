class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Helper method to add nodes at the end
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Helper method to print the list
    def display(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.val))
            temp = temp.next
        print(" -> ".join(elements) if elements else "Empty List")

    # Step-by-step: Find middle node using count // 2
    def find_middle(self):
        if not self.head:
            print("List is empty!")
            return

        # 1. Count total nodes
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next

        # 2. Traverse to the middle index
        mid_index = count // 2
        temp = self.head
        for _ in range(mid_index):
            temp = temp.next

        print(f"Middle node value: {temp.val}")
        return temp.val

    # Find and delete the middle node
    def delete_middle(self):
        if not self.head:
            print("List is empty!")
            return

        # Only 1 node
        if not self.head.next:
            self.head = None
            return

        # 1. Count total nodes
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next

        # 2. Stop at the node right before the middle
        mid_index = count // 2
        temp = self.head
        for _ in range(mid_index - 1):
            temp = temp.next

        # 3. Skip the middle node to delete it
        temp.next = temp.next.next

    # Delete both first and last nodes
    def delfirst_last(self):
        if not self.head:
            print("List is empty!")
            return

        # If only 1 or 2 nodes exist, removing both ends leaves an empty list
        if not self.head.next or not self.head.next.next:
            self.head = None
            return

        # 1. Delete first node
        self.head = self.head.next

        # 2. Delete last node
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


# --- Example Test Run ---
ll = SinglyLinkedList()

# Build list: 10 -> 20 -> 30 -> 40 -> 50
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