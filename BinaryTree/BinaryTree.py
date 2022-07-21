from queue import Queue
from queue import Queue, LifoQueue
import queue


class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


def createTree(root: Node):
    q = Queue(0)
    q.put(root)
    while not q.empty():
        p = q.get()
        x = input(f'Enter left child of {p.data} : ')
        if(int(x) != -1):
            t = Node(x)
            p.left = t
            q.put(t)
        x = input(f'Enter right child of {p.data} : ')
        if(int(x) != -1):
            t = Node(x)
            p.right = t
            q.put(t)


def preOrder(treeNode: Node):
    if(treeNode):
        print(treeNode.data)
        preOrder(treeNode.left)
        preOrder(treeNode.right)


def postOrder(treeNode: Node):
    if(treeNode):
        postOrder(treeNode.left)
        postOrder(treeNode.right)
        print(treeNode.data)


def inOrder(treeNode: Node):
    if treeNode:
        inOrder(treeNode.left)
        print(treeNode.data)
        inOrder(treeNode.right)


def iterativePreorder(treeNode: Node):
    stack = LifoQueue(0)
    while treeNode or not stack.empty():
        if(treeNode):
            print(treeNode.data)
            # now store
            stack.put(treeNode)
            # now you can go
            treeNode = treeNode.left
        else:
            # pop out and go to right side
            treeNode = stack.get()
            treeNode = treeNode.right


def iterativeInOrder(treeNode: Node):
    stack = LifoQueue(0)
    while treeNode or not stack.empty():
        if(treeNode):
            stack.put(treeNode)
            treeNode = treeNode.left
        else:
            treeNode = stack.get()
            # print(treeNode)
            print(treeNode.data)
            treeNode = treeNode.right


stack = []


def peek(stack):
    return stack[-1]


def iterativePostOrder(treeNode):
    while True:
        # print(stack)
        while(treeNode):
            stack.append(treeNode)
            stack.append(treeNode)
            treeNode = treeNode.left
        if(len(stack) == 0):
            return

        treeNode = stack.pop()

        if(len(stack) > 0 and treeNode == peek(stack)):
            treeNode = treeNode.right
        else:
            print(treeNode.data)
            treeNode = None


def levelOrder(treeNode):
    q = Queue(0)
    q.put(treeNode)
    while not q.empty():
        t = q.get()
        print(t.data)
        if(t.left):
            q.put(t.left)
        if(t.right):
            q.put(t.right)
# User function Template for python3


class Solution:

    # Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root):
        # Your code here
        d = {}
        q = Queue()
        if not root:
            return []
        q.put((root, 0))
        while not q.empty():
            root, hd = q.get()
            if not hd in d:
                d[hd] = []
            d[hd].append(root.data)
            if root.left:
                q.put((root.left, hd-1))
            if root.right:
                q.put((root.right, hd+1))
        res = []
        for _, v in sorted(d.items()):
            res.extend(v)
        return res



    from collections import deque
def reverseLevelOrder(root):
    # code here
    q=deque()
    q.append(root)
    ans=deque()
    while len(q):
        node= q.popleft()
        
        ans.appendleft(node.data)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    return ans
    pass


def count(treeNode):
    if(treeNode):
        x = count(treeNode.left)
        y = count(treeNode.right)
        return x+y+1
    return 0


def diameter(root):
    # Code here
    res = []

    def recur_find(node):
        if node:
            x = recur_find(node.left)
            y = recur_find(node.right)
            res.append(x+y+1)
            if(x > y):
                return x+1
            else:
                # res.append(x+y+1)
                return y+1
        return 0
    recur_find(root)
    return max(res)


class Solution:

    # Function to return the diameter of a Binary Tree.
    def diameter(self, root):
        # Code here
        maxDia = [0]

        def height(root, maxDia):
            if not root:
                return 0
            if root:
                x = height(root.left, maxDia)
                y = height(root.right, maxDia)
                maxDia[0] = max(maxDia[0], x+y+1)
                return max(x, y)+1
        height(root, maxDia)
        return maxDia[0]


def mirrorify(root):
    if(root):
        mirrorify(root.left)
        mirrorify(root.right)
        root.left, root.right = root.right, root.left


def topView(root):
    q = Queue(0)
    hd = 0
    m = dict()
    root.hd = 0
    q.put(root)
    while not q.empty():
        root = q.get()
        hd = root.hd
        if hd not in m:
            m[hd] = root.data
        if root.left:
            root.left.hd = hd-1
            q.put(root.left)
        if root.right:
            root.right.hd = hd+1
            q.put(root.right)
    res = []
    # print(m)
    for i in sorted(m):
        res.append(m[i])
    return res


def bottomView(root):
    q = []
    hd = 0
    m = dict()
    root.hd = 0
    q.append(root)
    while len(q):
        root = q[0]
        hd = root.hd
        m[hd] = root.data
        if root.left:
            root.left.hd = hd-1
            q.append(root.left)
        if root.right:
            root.right.hd = hd+1
            q.append(root.right)
        q.pop(0)
    res = []
    for i in sorted(m):
        res.append(m[i])
    return res


def zigZag(root):
    current_level = []
    next_level = []
    current_level.append(root)
    ltr = True
    res = []
    while len(current_level):
        temp = current_level.pop()
        res.append(temp.data)
        if ltr:
            if temp.left:
                next_level.append(temp.left)
            if temp.right:
                next_level.append(temp.right)
        else:
            if temp.right:
                next_level.append(temp.right)
            if temp.left:
                next_level.append(temp.left)
        if(not len(current_level)):
            ltr = not ltr
            current_level, next_level = next_level, current_level
    return res


def height(root):
    if root:
        X = height(root.left)
        Y = height(root.right)
        if(X > Y):
            return X+1
        else:
            return Y+1
    return 0


def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    l = isBalanced(root.left)
    r = isBalanced(root.right)
    if abs(lh-rh) <= 1:
        return l and r
    return False


def diagonal(root):
    #:param root: root of the given tree.
    # return: print out the diagonal traversal,  no need to print new line
    # code here
    res = []
    q = []
    q.append(root)
    res.append(root.data)
    while len(q):
        while root and root.right:
            q.append(root.right)
            res.append(root.right.data)
            root = root.right
        root = q.pop(0)
        root = root.left
        if root:
            q.append(root)
            res.append(root.data)
    return res


def printLevel(root, level, res):
    if root:
        if level == 1:
            res.append(root.data)
        else:
            printLevel(root.left, level-1, res)
            printLevel(root.right, level-1, res)


def reverseLevelOrder(root):
    h = height(root)
    res = []
    for i in reversed(range(1, h+1)):
        printLevel(root, i, res)
    print(res)


def findIndex(str, si, ei):
    s = []
    index = si
    while index <= ei:
        if str[index] == '(':
            s.append('(')
        elif str[index] == ')':
            if s[-1] == '(':
                s.pop()
            if len(s) == 0:
                return index
        index += 1
    return -1


def fromString(str, si, ei):
    if si > ei:
        return None
    root = Node(int(str[si]))
    index = -1
    if si+1 < ei and str[si+1] == '(':
        index = findIndex(str, si+1, ei)
    if index != -1:
        root.left = fromString(str, si+2, index-1)
        root.right = fromString(str, index+2, ei-1)
    return root


class Solution:
    def printLeaves(self, root, res):
        if root:
            self.printLeaves(root.left, res)
            self.printLeaves(root.right, res)
            if not root.left and not root.right:
                res.append(root.data)

    def printLeft(self, root, res):
        if root:
            if root.left:
                res.append(root.data)
                self.printLeft(root.left, res)
            elif root.right:
                res.append(root.data)
                self.printLeft(root.right, res)

    def printRight(self, root, res):
        if root:
            if root.right:
                self.printRight(root.right, res)
                res.append(root.data)
            elif root.left:
                self.printRight(root.left, res)
                res.append(root.data)

    def printBoundaryView(self, root):
        # Code here
        res = [root.data]
        if root and (root.left or root.right):
            self.printLeft(root.left, res)
            self.printLeaves(root, res)
            self.printRight(root.right, res)
        return res


def sumTree(root):
    if not root:
        return 0
    old_val = root.data
    root.data = sumTree(root.left)+sumTree(root.right)
    return root.data+old_val


def searchInOrder(in_order, start, end, key):
    for i in range(start, end+1):
        if in_order[i] == key:
            return i

def treeFromPreIn(in_order, pre_order, end, start=0):
    if start > end:
        return None
    root = Node(pre_order[treeFromPreIn.pre_index])
    treeFromPreIn.pre_index += 1
    if start == end:
        return root
    splitIndex = searchInOrder(in_order, start, end, root.data)
    root.left = treeFromPreIn(in_order, pre_order, splitIndex-1, start)
    root.right = treeFromPreIn(in_order, pre_order, end, splitIndex+1)
    return root

def sumToRootLongest(root):
    def util(root, level, sum, maxlevel, maxsum):
        if not root:
            if level > maxlevel[0]:
                maxlevel[0] = level
                maxsum[0] = sum
            elif level == maxlevel[0] and sum > maxsum[0]:
                maxsum[0] = sum
            return

        util(root.left, level+1, sum+root.data, maxlevel, maxsum)
        util(root.right, level+1, sum+root.data, maxlevel, maxsum)

    if not root:
        return 0
    level = 0
    sum = 0
    maxlevel = [0]
    maxsum = [-999999999999]
    util(root, level, sum, maxlevel, maxsum)
    return maxsum[0]


def largestSubTreeSum(root):
    if not root:
        return 0

    def util(root, res):
        if not root:
            return 0
        old_val = root.data
        x = util(root.left, res) + util(root.right, res)+old_val
        res.append(x)
        return x

    res = []
    util(root, res)
    return max(res)


def allKSumPaths(root, k):
    def printPath(path, j):
        for i in range(j, len(path)):
            print(path[i], sep=' ')

    def util(root, k, path):
        if not root:
            return
        # preorder
        path.append(root.data)
        util(root.left, k, path)
        util(root.right, k, path)

        f = 0
        for i in range(len(path)-1, -1, -1):
            f += path[i]
            if f == k:
                printPath(path, i)
        path.pop(-1)
    path = []
    util(root, k, path)


class Solution:
    def sum(self, root):
        if not root:
            return 0
        return (self.sum(root.left) + root.data + self.sum(root.right))

    def isSumTree(self, root):
        if not root or (not root.left and not root.right):
            return 1
        ls = self.sum(root.left)
        rs = self.sum(root.right)
        if root.data == ls+rs and self.isSumTree(root.left) and self.isSumTree(root.right):
            return 1
        else:
            return 0


class Solution:
    #Function to return maximum path sum from any node in a tree.
    def util(self, root, maxTill):
        if not root:
            return 0
        if not root.left and not root.right:
            maxTill[0]=max(maxTill[0], root.data)
            return root.data
        lSum=max(0,self.util(root.left, maxTill))
        rSum=max(0,self.util(root.right, maxTill))
        
        maxTill[0]=max(maxTill[0], root.data+lSum+rSum)
        return root.data+max(lSum, rSum) 
    def findMaxSum(self, root): 
        #Your code here
        maxTill=[-float('inf')]
        self.util(root, maxTill)
        return maxTill[0]

# Level order


class Solution:
    # Function to return the level order traversal of a tree.
    def levelOrder(self, root):
        # Code here
        q = Queue()
        res = []
        q.put(root)
        while not q.empty():
            root = q.get()
            res.append(root.data)
            if root.left:
                q.put(root.left)
            if root.right:
                q.put(root.right)
        return res


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 1
        q = Queue()
        res = []
        q.put((root, level))
        while not q.empty():
            root, curLevel = q.get()
            if len(res) < curLevel:
                res.append([])
            res[-1].append(root.val)
            if root.left:
                q.put((root.left, curLevel+1))
            if root.right:
                q.put((root.right, curLevel+1))
        return res

# LCA


# User function Template for python3

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''


class Solution:
    def findPath(self, root, n, path):
        if not root:
            return False
        if root.data == n:
            path.append(root)
            return True
        path.append(root)
        if root.left and self.findPath(root.left, n, path):
            return True
        if root.right and self.findPath(root.right, n, path):
            return True
        path.pop()
        return False

    # Function to return the lowest common ancestor in a Binary Tree.
    def lca(self, root, n1, n2):
        # Code here
        path1 = []
        path2 = []
        if not self.findPath(root, n1, path1):
            return -1
        if not self.findPath(root, n2, path2):
            return -1
        i = 0
        # print(path1)
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]


# root=Node(10)
# root.left=Node(4)
# root.right=Node(8)
# root.left.left=Node(2)
# root.left.right=Node(3)
# root.right.left=Node(7)
# root.right.right=Node(9)
# str='4(2(3)(1))(6(5))'
root = Node(10)
root.left = Node(-2)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(-4)
root.right.left = Node(7)
root.right.right = Node(5)

in_order = [3, 1, 4, 0, 5, 2]
pre_order = [0, 1, 3, 4, 2, 5]
treeFromPreIn.pre_index = 0
root = treeFromPreIn(in_order, pre_order, 5, 0)
postOrder(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def LeftView(root):
    res = []
    levels = set()

    def util(root, level):
        if root:
            if not level in levels:
                res.append(root.data)
                levels.add(level)
            util(root.left, level+1)
            util(root.right, level+1)
    util(root, 0)
    return res


def LeftView(root):
    d = {'traversed_level': 0}
    res = []

    def leftViewRecur(root, current_level=0):

        if root:
            if d['traversed_level'] == current_level:
                res.append(root.data)
                d['traversed_level'] += 1
            leftViewRecur(root.left, current_level+1)
            leftViewRecur(root.right, current_level+1)
    leftViewRecur(root, 0)
    return res


# Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self, root):

        def height(root):
            if not root:
                return 0
            if root:
                leftHeight = height(root.left)
                if leftHeight == -1:
                    return -1
                rightHeight = height(root.right)
                if rightHeight == -1:
                    return -1
                if abs(leftHeight-rightHeight) > 1:
                    return -1
                return max(leftHeight, rightHeight)+1

        return True if height(root) != -1 else False


class Solution:
    def morrisinorderTraversal(self, root):
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre.right is not None and pre.right != root:
                    pre = pre.right
                if pre.right == root:
                    pre.right = None
                    res.append(root.val)
                    root = root.right
                else:
                    pre.right = root
                    root = root.left
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def morrispreorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre.right is not None and pre.right != root:
                    pre = pre.right
                if pre.right == None:
                    pre.right = root
                    res.append(root.val)
                    root = root.left
                else:
                    pre.right = None
                    root = root.right
        return res
#! Path to given node
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def inorder(self, root, B, path):
        if not root:
            return False
        if root.val == B:
            path.append(root.val)
            return True
        path.append(root.val)
        if root.left:
            if self.inorder(root.left, B, path):
                return True
        if root.right:
            if self.inorder(root.right, B, path):
                return True
        path.pop()
        return False

    def solve(self, A, B):
        path = []
        self.inorder(A, B, path)
        return path if len(path) else -1
# preOrder(fromString(str, 0, len(str)-1))
# print(printBoundary(root))
# sumTree(root)
# preOrder(root)
# print(topView(root))
# inOrder(root)
# mirrorify(root)
# print('')
# inOrder(root)
# reverseLevelOrder(root)
# print(zigZag(root))
# print(isBalanced(root))

# createTree(root)
# preOrder(root)
# postOrder(root)
# print(count(root))
# print(diameter(root))

# levelOrder(root)
# iterativePostOrder(root)

# iterativePostOrder(root)
