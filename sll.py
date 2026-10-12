#Traversing the elements of the linked list
# Create Linked List
# Traverse and print the node values
# Insert node at a specific position
# Find Middle node and print its value
# Delete node
# Reverse list
# Calculate the sum of every two consecutive node values.

class Node :
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# Traverse and print the node values

    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data  , end=" -> ")
            temp = temp.next
        print("None")

    def insertion(self , pos , val):
        new_node = self.head
        if pos == 0:
            self.head = new_node
            return 
        temp = self.head
        for _ in range(pos-1):
            if temp is None:
                print("Postion is out of range ")
                






    
    