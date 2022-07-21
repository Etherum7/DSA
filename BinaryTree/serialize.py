# User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Function to serialize a tree and return a list containing nodes of tree.


def serialize(root, A):
    # code here
    if not root:
        A.append('N')
        return
    A.append(root.data)
    serialize(root.left, A)
    serialize(root.right, A)

# Function to deserialize a list and construct the tree.


def deSerialize(A):
    # code here
    i = 0

    def createNode():
        nonlocal i
        val = A[i]
        i += 1
        if val == 'N':
            return None
        node = Node(val)
        node.left = createNode()
        node.right = createNode()
        return node
    return createNode()
