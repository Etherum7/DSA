# User function Template for python3
t = {}


def LISS(root):
    # code here
    if not root:
        return 0
    if root in t:
        return t[root]
    if (root.left == None and
            root.right == None):
        t[root] = 1

        return 1
    a = 1
    if root.left:
        a += LISS(root.left.left)+LISS(root.left.right)
    if root.right:
        a += LISS(root.right.left)+LISS(root.right.right)
    b = LISS(root.left)+LISS(root.right)
    t[root] = max(a, b)
    return t[root]


class node:
    def __init__(self):
        self.data = 0
        self.liss = 0
        self.left = self.right = None


def newNode(data):
    temp = node()
    temp.data = data
    temp.left = temp.right = None
    return temp


root = newNode(20)
root.left = newNode(8)
root.left.left = newNode(4)
root.left.right = newNode(12)
root.left.right.left = newNode(10)
root.left.right.right = newNode(14)
root.right = newNode(22)
root.right.right = newNode(25)
print(LISS(root))
