#W.A.P to count occurance of a number in the Dobly linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None
    def print(self):
        print(self.data, end=" ")
    def get_data(self):
        return self.data
    def count_occurrences(self, value):
        count = 0
        current = self
        while current is not None:
            if current.data == value:
                count += 1
            current = current.next
        return count
    