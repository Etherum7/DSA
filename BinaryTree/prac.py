from collections import deque
from queue import Queue

# from BinaryTree.BinaryTree import preOrder


class Node:
    def __init__(self, data=0):
        self.data = data
        self.right = None
        self.left = None
class temp:
    def iterPreorder(self, root):
        st=[]
        while root or len(st):
            if root:
                print(root.data)
                st.append(root)
                root=root.left
            else:
                root=st.pop()
                root=root.right
    def iterInOrder(self, root):
        st=[]
        while root or len(st):
            if root:
                st.put(root)
                root=root.left
            else:
                root=st.pop()
                print(root.data)
                root=root.right
    def iterPostorder(self, root):
        st=[]
        while True:
            while root :
                
                    st.append(root)
                    st.append(root)
                    root=root.left
            if len(st)==0:
                return
            
            root=st.pop()
            if len(st) and root==st[-1]:
                root=root.right
            else:
                print(root.data)
                root=None

root = Node(10)
root.left = Node(-2)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(-4)
root.right.left = Node(7)
root.right.right = Node(5)
ob=temp()
ob.iterPostorder(root)



# class Solution:
#     def bottomView(self, root):
#         # code here
#         q = Queue()
#         res = []
#         d = {}
#         q.put((root, 0))
#         while not q.empty():
#             root, hd = q.get()
#             d[hd] = root.data
#             if root.left:
#                 q.put((root.left, hd-1))
#             if root.right:
#                 q.put((root.right, hd+1))
#         # print(d)
#         for _, v in sorted(d.items()):
#             res.append(v)
#         return res


# class Solution:

#     # Function to return a list of nodes visible from the top view
#     # from left to right in Binary Tree.
#     # level order but don;t overwrite
#     def topView(self, root):
#         q = Queue()
#         q.put((root, 0))
#         d = {}
#         res = []
#         while not q.empty():
#             root, hd = q.get()
#             if hd not in d:
#                 d[hd] = root.data
#             if root.left:
#                 q.put((root.left, hd-1))
#             if root.right:
#                 q.put((root.right, hd+1))
#         for _, v in sorted(d.items()):
#             res.append(v)
#         return res
# # All Paths are
# # User function Template for python3

# # User function Template for python3


# '''
# class Node:
#     def _init_(self,val):
#         self.data=val
#         self.left=None
#         self.right=None
# '''


# def util(root, res, op):
#     if not root:
#         return
#     if not root.left and not root.right:
#         op.append(root.data)
#         res.append(op.copy())
#         op.pop()
#         return
#     op.append(root.data)
#     if root.left:
#         util(root.left, res, op)
#     if root.right:
#         util(root.right, res, op)
#     op.pop()


# def Paths(root):
#     # don't print new line
#     res = []
#     util(root, res, [])
#     return res
# # Height


# class Solution:
#     # Function to find the height of a binary tree.
#     def height(self, root):
#         # code here
#         if not root:
#             return 0
#         return max(self.height(root.left), self.height(root.right))+1


# class Solution:
#     # Function to check if two trees are identical.
#     def isIdentical(self, root1, root2):
#         # Code here
#         if root1 == None and root2 == None:
#             return True
#         if root1 == None or root2 == None:
#             return False
#         return root1.data == root2.data and (self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right))
# # Bad


# class Solution:
#     # Function to check if two trees are identical.
#     def inorder(self, root, res):
#         if root:
#             self.inorder(root.left, res)
#             res.append(root.data)
#             self.inorder(root.right, res)

#     def preorder(self, root, res):
#         if root:
#             res.append(root.data)
#             self.preorder(root.left, res)

#             self.preorder(root.right, res)

#     def isIdentical(self, root1, root2):
#         # Code here
#         inorder1 = []
#         inorder2 = []
#         self.inorder(root1, inorder1)
#         self.inorder(root2, inorder2)
#         if len(inorder1) != len(inorder2):
#             return False
#         for i in range(len(inorder1)):
#             if inorder1[i] != inorder2[i]:
#                 return False
#         preorder1 = []
#         preorder2 = []
#         self.preorder(root1, preorder1)
#         self.preorder(root2, preorder2)
#         for i in range(len(preorder1)):
#             if preorder1[i] != preorder2[i]:
#                 return False
#         return True

# Tree from inorder and postorder


class Solution:
    def searchInOrder(self, inorder, inStart, inEnd, val):
        for i in range(inStart, inEnd+1):
            if inorder[i] == val:
                return i
        return -1

    def generateTree(self, inorder, preorder, inStart, inEnd, preIndex):
        if inStart > inEnd:
            return None
        node = Node(preorder[preIndex[0]])
        preIndex[0] += 1
        if inStart == inEnd:
            return node
        splitIndex = self.searchInOrder(inorder, inStart, inEnd, node.data)
        node.left = self.generateTree(
            inorder, preorder, inStart, splitIndex-1, preIndex)
        node.right = self.generateTree(
            inorder, preorder, splitIndex+1, inEnd, preIndex)
        return node

    def postOrder(self, root, res):
        if root:
            self.postOrder(root.left, res)
            self.postOrder(root.right, res)
            res.append(root.data)

    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root node
        preIndex = [0]

        root = self.generateTree(inorder, preorder, 0, n-1, preIndex)
        res = []
        self.postOrder(root, res)
        return res


ob = Solution()
# print(ob.buildtree([10, 1, 30, 40, 20],
#                    [1, 10, 20, 30, 40], 5))


def searchInOrder(In, inStart, inEnd, val):
    for i in range(inStart, inEnd+1):
        if In[i] == val:
            return i
    return -1


def generateTree(In, post, inStart, inEnd, postIndex):
    if inStart > inEnd:
        return None
    node = Node(post[postIndex[0]])
    postIndex[0] -= 1
    if inStart == inEnd:
        return node
    splitIndex = searchInOrder(In, inStart, inEnd, node.data)
    node.right = generateTree(In, post, splitIndex+1, inEnd, postIndex)
    node.left = generateTree(In, post, inStart, splitIndex-1, postIndex)

    return node


def buildTree(In, post, n):
    # your code here
    inStart = 0
    inEnd = n-1
    postIndex = [n-1]
    root = generateTree(In, post, inStart, inEnd, postIndex)
    return root


print(buildTree([4, 8, 2, 5, 1, 6, 3, 7], [8, 4, 5, 2, 6, 7, 3, 1], 8))

# Symetric
# bool isSymmetricUtil(node * root1, node * root2) {
#   if (root1 == NULL || root2 == NULL)
#     return root1 == root2;
#   return (root1 -> data == root2 -> data) && isSymmetricUtil(root1 -> left, root2->
#   right) && isSymmetricUtil(root1 -> right, root2 -> left);
# }
# bool isSymmetric(node * root) {
#   if (!root) return true;
#   return isSymmetricUtil(root -> left, root -> right);
# }

# class Solution:
# return true/false denoting whether the tree is Symmetric or not


def inOrder(self, root, res):
    if root:
        self.inOrder(root.left, res)
        res.append(root.data)
        self.inOrder(root.right, res)


def isSymmetric(self, root):
    # Your Code Here
    in1 = []
    in2 = []
    if not root or (not root.left and not root.right):
        return True
    self.inOrder(root.left, in1)
    self.inOrder(root.right, in2)
    n = len(in1)
    m = len(in2)
    if n != m:
        return False
    for i in range(n):
        if in1[i] != in2[n-i-1]:
            return False
    return True


class Solution:
    # Function to convert a binary tree into its mirror tree.
    def swap(self, root):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp

    def mirror(self, root):
        # Code here
        q = deque()
        q.append(root)

        while len(q):
            node = q.pop()
            self.swap(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


# children sum parent
'''

    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''


def modifyDFS(root):
    if not root:
        return 0
    if root:
        lSum = rSum = 0
        if root.left:
            lSum = root.left.data
        if root.right:
            rSum = root.right.data
        childSum = lSum+rSum
        if childSum == 0:
            return
        if childSum < root.data:
            if root.left:
                root.left.data = root.data
            if root.right:
                root.right.data = root.data
        modifyDFS(root.left)
        modifyDFS(root.right)
        tot = 0
        if root.left:
            tot += root.left.data
        if root.right:
            tot += root.right.data
        if root.left or root.right:
            root.data = tot


def changeTree(root):
    # Write your code here.
    modifyDFS(root)
    return root


class Solution:
    # Function to check whether all nodes of a tree have the value
    # equal to the sum of their child nodes.
    def sumChild(self, root):

        if root:
            lSum = self.sumChild(root.left)
            if lSum == -1:
                return -1
            rSum = self.sumChild(root.right)
            if rSum == -1:
                return -1
            if lSum == 0 and rSum == 0:
                return root.data
            if lSum+rSum == root.data:
                return root.data
            return -1
        return 0

    def isSumProperty(self, root):
        # code here
        ind = self.sumChild(root)
        return 1 if ind != -1 else 0
# Flatten


class Solution:
    def join(self, root1, root2):
        while root1.right != None:
            root1 = root1.right
        root1.right = root2

    def swap(self, root):
        if root.left:
            root.right = root.left
            root.left = None

    def flatten(self, root):
        # code here
        if root:
            if root.right:
                if root.left:
                    self.join(root.left, root.right)
            self.swap(root)
            self.flatten(root.right)
