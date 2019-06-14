class Node:
    def __init__(self,value=None,lchild=None,rchild=None):
        self.value = value
        self.left = lchild
        self.right = rchild


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []

    def add(self,v):
        new = Node(value=v)
        self.queue.append(new)
        if self.root == None :
            self.root = new
        else:
            node = self.queue[0]
            if node.left == None:
                node.left = new
            else:
                node.right = new
                self.queue.pop(0)
    def front_print(self, node):
        s = []
        n = node 
        while s or n:
            while n:
                print(n.value, end=" ")
                s.append(n)
                n = n.left
            n = s.pop()
            n = n.right
    def front_order(self,node):
        if node == None:
            return
        print(node.value, end=" ")
        self.front_order(node.left)
        self.front_order(node.right)
    def middle_order(self,node):
        if node == None:
            return
        self.middle_order(node.left)
        print(node.value, end=" ")
        self.middle_order(node.right)
t = Tree()
for i in range(1,10):
    t.add(i)
t.middle_order(t.root)