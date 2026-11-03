class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class
class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)
        new.next = self.top
        self.top = new

    def pop(self):
        x = self.top.data
        self.top = self.top.next
        return x


# Queue class
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new = Node(x)

        if self.front == None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def dequeue(self):
        if self.front == None:
            print("Empty")
        else:
            print("Deleted:", self.front.data)
            self.front = self.front.next

            if self.front == None:
                self.rear = None

    def display(self):
        temp = self.front

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # Reverse using Stack
    def reverse(self):
        s = Stack()

        temp = self.front

        while temp != None:
            s.push(temp.data)
            temp = temp.next

        self.front = self.rear = None

        while s.top != None:
            self.enqueue(s.pop())

    # Merge two queues
    def merge(self, q2):
        temp = q2.front

        while temp != None:
            self.enqueue(temp.data)
            temp = temp.next

    # Check identical
    def identical(self, q2):
        a = self.front
        b = q2.front

        while a != None and b != None:
            if a.data != b.data:
                print("Not Identical")
                return

            a = a.next
            b = b.next

        if a == None and b == None:
            print("Identical")
        else:
            print("Not Identical")


# Main program
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:")
q.display()

print("Dequeue:")
q.dequeue()

print("Reverse:")
q.reverse()
q.display()

q2 = Queue()
q2.enqueue(40)
q2.enqueue(50)

print("Merge:")
q.merge(q2)
q.display()

print("Identical:")
q.identical(q2)