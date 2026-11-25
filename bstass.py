
class Node:
    def __init__(self, value):
        self.left = None
        self.pid = value
        self.right = None


class BST:
    def __init__(self):
        self.rt = None

    def insert(self, new_node):
        if self.rt is None:
            self.rt = new_node
        else:
            temp = self.rt
            while True:
                if new_node.pid < temp.pid:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.pid, end=" ")
        self.inorder(rt.right)

    def search(self, value):
        temp = self.rt
        while temp is not None:
            if value == temp.pid:
                return True
            elif value < temp.pid:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def delete(self, rt, value):
        if rt is None:
            return rt

        if value < rt.pid:
            rt.left = self.delete(rt.left, value)
        elif value > rt.pid:
            rt.right = self.delete(rt.right, value)
        else:
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left

            succ = self.get_successor(rt)
            rt.pid = succ.pid
            rt.right = self.delete(rt.right, succ.pid)

        return rt

    def get_successor(self, rt):
        temp = rt.right
        while temp.left is not None:
            temp = temp.left
        return temp

    def preorder(self, rt):
        if rt is None:
            return

        print(rt.pid, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return

        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.pid, end=" ")

    def MinMax(self, rt):
        temp = self.rt
        while temp.left:
            temp = temp.left
        print("\nMin Product Id:", temp.pid)

        temp = self.rt
        while temp.right:
            temp = temp.right
        print("Max Product Id:", temp.pid)


# Main program

b1 = BST()

b1.insert(Node(150))
b1.insert(Node(100))
b1.insert(Node(200))
b1.insert(Node(75))
b1.insert(Node(125))
b1.insert(Node(175))
b1.insert(Node(250))
b1.insert(Node(60))
b1.insert(Node(90))
b1.insert(Node(110))

print("\nProduct ID in Ascending Order:")
b1.inorder(b1.rt)

print("\n\nSearch for Product ID 175:")
if b1.search(175):
    print("Product ID Found")
else:
    print("Product ID Not Found")

b1.MinMax(b1.rt)

b1.rt = b1.delete(b1.rt, 100)

print("\nUpdated Product IDs:")
b1.inorder(b1.rt)
