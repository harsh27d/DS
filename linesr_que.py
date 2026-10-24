#Linear queue using linked list 
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class lqueue:
    def __init__(self):
        self.front=self.rear =None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
             self.front = self.rear = new_node
    def dequeue(self):
        temp = self.front
        print("deleted the Node: ", temp.data)
        self.front=self.front.next
        if self.front is None:# if there is only one node
             print("Queue is empty")
             self.rear=None
        temp=None
    def print(self):
        temp = self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
            print()
que= lqueue()
que.enqueue(Node(23))
que.enqueue(Node(30))
que.enqueue(Node(40))
que.enqueue(Node(50))
que.print()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
