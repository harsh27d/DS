class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_alternate_nodes(head):
    if not head:
        return None

    current = head
    while current and current.next:
        current.next = current.next.next
        current = current.next
    return head


def print_list(head):
    current = head
    values = []
    while current:
        values.append(str(current.data))
        current = current.next
    print(" -> ".join(values) if values else "None")


if __name__ == "__main__":
    ll = Node(1)
    ll.next = Node(2)
    ll.next.next = Node(3)
    ll.next.next.next = Node(4)
    ll.next.next.next.next = Node(5)

    print("Original List:")
    print_list(ll)
    delete_alternate_nodes(ll)
    print("List after deleting alternate nodes:")
    print_list(ll)