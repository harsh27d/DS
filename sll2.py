class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_first_and_last(head):
    # If list has 0, 1, or 2 nodes, removing first and last leaves an empty list
    if not head or not head.next or not head.next.next:
        return None

    # Step 1: Remove first node
    head = head.next

    # Step 2: Stop at the second-to-last node and remove the last node
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None

    return head


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# --- Test ---
# Build list: 1 -> 2 -> 3 -> 4 -> 5
ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)

print("Original List:")
print_list(ll)

ll = delete_first_and_last(ll)

print("List after deleting first and last nodes:")
print_list(ll)