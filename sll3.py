class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_alternate_nodes(head):
    if not head:
        return None

    current = head
    # Skip every second node
    while current and current.next:
        current.next = current.next.next
        current = current.next

    return head


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# --- Test Run ---
# Create list: 1 -> 2 -> 3 -> 4 -> 5
ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
ll.next.next.next.next = Node(5)

print("Original List:")
print_list(ll)

# Delete alternate nodes (removes 2 and 4)
delete_alternate_nodes(ll)

print("List after deleting alternate nodes:")
print_list(ll)