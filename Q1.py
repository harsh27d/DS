class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top == None:
            print("Stack is empty")
            return None

        x = self.top.data
        self.top = self.top.next
        return x

    def display(self):
        temp = self.top

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def reverse_string(self, s):
        temp = Stack()

        for ch in s:
            temp.push(ch)

        while temp.top != None:
            print(temp.pop(), end="")

        print()

    def reverse_stack(self):
        temp = Stack()

        while self.top != None:
            temp.push(self.pop())

        self.top = temp.top


# Main program
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
s.pop()
s.display()

s.reverse_string("hello")

s.reverse_stack()
s.display()