class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_first_and_last(head):
    if not head or not head.next or not head.next.next:
        return None

    head = head.next
    curr = head
    while curr.next and curr.next.next:
        curr = curr.next
    curr.next = None
    return head


def print_list(head):
    curr = head
    values = []
    while curr:
        values.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(values) if values else "None")


if __name__ == "__main__":
    ll = Node(1)
    ll.next = Node(2)
    ll.next.next = Node(3)
    ll.next.next.next = Node(4)
    ll.next.next.next.next = Node(5)

    print("Original List:")
    print_list(ll)

    ll = delete_first_and_last(ll)
    print("List after deleting first and last nodes:")
    print_list(ll)