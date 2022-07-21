# # Connect at same
# from collections import deque


# class Solution:
#     # Function to connect nodes at same level.
#     def connect(self, root):
#         q = deque()
#         q.append((root, 0))
#         while len(q):
#             (root, level) = q.popleft()
#             if len(q) == 0 or q[0][1] != level:
#                 root.nextRight = None
#             elif q[0][1] == level:
#                 root.nextRight = q[0][0]
#             if root.left:
#                 q.append((root.left, level+1))
#             if root.right:
#                 q.append((root.right, level+1))
# # If leaves at same level, then Ciomplete BT


# class Solution:
#     # Function to connect nodes at same level.
#     def connectRecur(self, root):
#         if not root:
#             return
#         if root.left:
#             root.left.nextRight = root.right
#         if root.right:
#             if root.nextRight:
#                 root.right.nextRight = root.nextRight.left
#             else:
#                 root.right.nextRight = None
#         self.connectRecur(root.left)
#         self.connectRecur(root.right)

#     def connect(self, root):
#         root.nextRight = None
#         self.connectRecur(root)
# # Sorted array to bst


# class Solution:
#     def connectRecur(self, nums, start, end):
#         if start > end:
#             return None
#         mid = (start+end)//2
#         node = TreeNode(nums[mid])
#         if start == end:
#             return node
#         node.left = self.connectRecur(nums, start, mid-1)
#         node.right = self.connectRecur(nums, mid+1, end)
#         return node

#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         n = len(nums)
#         mid = n//2
#         root = TreeNode(nums[mid])
#         start = 0
#         end = n-1
#         root.left = self.connectRecur(nums, start, mid-1)
#         root.right = self.connectRecur(nums, mid+1, end)
#         return root
# # Check for BST


# class Solution:

#     # Function to check whether a Binary Tree is BST or not.
#     def isBSTutil(self, root, mn, mx):
#         if not root:
#             return True
#         if mn < root.data < mx:
#             validLeft = self.isBSTutil(root.left, mn, root.data)
#             if not validLeft:
#                 return False
#             validRight = self.isBSTutil(root.right, root.data, mx)
#             if not validRight:
#                 return False
#             return True
#         else:
#             return False

#     def isBST(self, root):
#         # code here
#         return self.isBSTutil(root, -float('inf'), float('inf'))
# # LCA to


# def LCA(root, n1, n2):
#     # code here.
#     while root:
#         if root.data < n1 and root.data < n2:
#             root = root.right
#         elif n1 < root.data and n2 < root.data:
#             root = root.left
#         else:
#             return root
#     return None


# def path(root, n, res):
#     if root:
#         res.append(root)
#         if root.data == n:
#             return True
#         if n < root.data:
#             return path(root.left, n, res)
#         else:
#             return path(root.right, n, res)
#         res.pop()
#         return False


# # Function to find the lowest common ancestor in a BST.
# def LCA(root, n1, n2):
#     path1 = []
#     path2 = []
#     i = 0
#     if not path(root, n1, path1) or not path(root, n2, path2):
#         return -1
#     while i < len(path1) and i < len(path2):
#         if path1[i] != path2[i]:
#             break
#         i += 1
#     return path1[i-1]

# # VImp


# def findPreSuc(root, pre, suc, key):
#     # your code goes here
#     if not root:
#         return
#     while root:
#         if root.key == key:
#             if root.left:
#                 tmp = root.left
#                 while tmp.right:
#                     tmp = tmp.right
#                 pre[0] = tmp
#             if root.right:
#                 tmp = root.right
#                 while tmp.left:
#                     tmp = tmp.left
#                 suc[0] = tmp
#             return
#         elif root.key > key:
#             suc[0] = root
#             root = root.left

#         else:
#             pre[0] = root
#             root = root.right
# # Floor


# from typing import Iterator


class TreeNode:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

# # Ceil


# def findCeil(root, x):
#     # Write your code here.
#     cel = -1
#     while root:
#         if root.data == x:
#             return x
#         elif root.data > x:
#             cel = root.data
#             root = root.left
#         else:
#             root = root.right
#     return cel


# def floorInBST(root, X):
#     # Write your Code here.
#     flr = 0
#     while root:
#         if root.data == X:
#             return root.data
#         elif root.data > X:
#             root = root.left
#         else:
#             flr = root.data
#             root = root.right
#     return flr
# # Kth smallest 01


# class Solution:
#     # Return the Kth smallest element in the given BST

#     def KthSmallestElement(self, root, K):
#         # code here.
#         cnt = 0
#         while root:
#             if not root.left:
#                 cnt += 1
#                 if cnt == K:
#                     return root.data
#                 root = root.right
#             else:
#                 tmp = root.left
#                 while tmp.right != None and tmp.right != root:
#                     tmp = tmp.right
#                 if tmp.right == root:
#                     tmp.right = None
#                     cnt += 1
#                     if cnt == K:
#                         return root.data
#                     root = root.right
#                 else:
#                     tmp.right = root
#                     root = root.left
#         return -1
# # kth largest


# class Solution:

#     def inorder(self, root, cnt):
#         if root:
#             val = self.inorder(root.right, cnt)
#             if val != -1:
#                 return val
#             cnt[0] -= 1
#             if cnt[0] == 0:
#                 return root.data
#             val = self.inorder(root.left, cnt)
#             if val != -1:
#                 return val
#         return -1

#     def kthLargest(self, root, k):
#         # your code here
#         cnt = [k]
#         return self.inorder(root, cnt)


# class Solution:
#     # Return the Kth smallest element in the given BST
#     def inorder(self, root, k, cnt):
#         if root:
#             val = self.inorder(root.left, k, cnt)
#             if val != -1:
#                 return val
#             cnt[0] += 1
#             if cnt[0] == k:
#                 return root.data
#             val = self.inorder(root.right, k, cnt)
#             if val != -1:
#                 return val
#         return -1

#     def KthSmallestElement(self, root, K):
#         # code here.

#         return self.inorder(root, K, [0])
# # Kth smallest bad


# class Solution:
#     # Return the Kth smallest element in the given BST

#     def inorder(self, root, res):

#         if root:
#             self.inorder(root.left, res)
#             res.append(root.data)
#             self.inorder(root.right, res)

#     def KthSmallestElement(self, root, K):
#         # code here.
#         res = []
#         self.inorder(root, res)
#         if K > len(res) or K < 1:
#             return -1
#         return res[K-1]

# # target sum


# class Solution:
#     # root : the root Node of the given BST
#     # target : the target sum O(n)
#     def inorder(self, root, target, s):
#         if not root:
#             return False

#         if self.inorder(root.left, target, s):
#             return True
#         if target-root.data in s:
#             return True
#         else:
#             s.add(root.data)
#         return self.inorder(root.right, target, s)

#     def isPairPresent(self, root, target):
#         # code here.
#         s = set()
#         return int(self.inorder(root, target, s))

# # BST Iterator# Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.head=root
#         self.stack=[]
#         self.push(root)
#     def push(self,root):
#         while root:
#             self.stack.append(root)
#             root=root.left

#     def next(self) -> int:

#         temp=self.stack.pop()
#         self.push(temp.right)
#         return temp.val


#     def hasNext(self) -> bool:
#         return len(self.stack)!=0
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(6)

# print(floorInBST(root, 7))


class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def getCount(self, root, mx):
        if not root:
            return 0
        lCount = self.getCount(root.left, mx)
        rCount = self.getCount(root.right, mx)
        curData = root.data
        leftValid = root.left and root.left.data < curData
        rightValid = root.right and root.right.data > curData
        if leftValid and rightValid:
            mx = max(lCount+rCount+1, mx)
            return lCount+rCount+1
        if leftValid:
            mx = max(mx, lCount+1)

            return lCount+1
        elif rightValid:
            mx = max(mx, rCount+1)
            return rCount+1
        else:
            mx = max(mx, 1)
            return 1

    def largestBst(self, root):
        # code here
        mx = [0]
        self.getCount(root, mx)
        return mx[0]
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)

Solution().largestBst(root)