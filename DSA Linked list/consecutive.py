#Print sum of 2 consecutive nodes in Singly linked List
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node  # appending the new node

    def print_sum_of_consecutive_nodes(self):
        temp = self.head
        while temp and temp.next:
            sum_consecutive = temp.data + temp.next.data
            print(f"Sum of {temp.data} and {temp.next.data} is: {sum_consecutive}")
            temp = temp.next        
# Create linked list
list = LinkedList()

# Append nodes
list.append(Node(5))
list.append(Node(10))
list.append(Node(15))
list.append(Node(-10))
list.append(Node(50))

# Print sum of consecutive nodes
list.print_sum_of_consecutive_nodes()
