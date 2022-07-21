import math


class Node:
    def __init__(self,data=0):
        self.left=None
        self.data=data
        self.right=None
        self.next=None
def insert(root, key):
    while root:
        t=root
        if root.data==key:
            return
        elif root.data<key:
            root=root.right
        else:
            root=root.left
    node = Node(key)
    if t.data<key:
        t.right=node
    else:
        t.left=node
def rInsert(root,key):
    if not root:
        return Node(key)
    else:
        if root.data==key:
            return root
        elif root.data> key:
            root.left= rInsert(root.left,key)
        else:
            root.right= rInsert(root.right,key)
    return root
def search(root, key):
    if root:
        if root.data==key:
            return root
        elif root.data< key:
            return search(root.right, key)
        else:
         return search(root.left, key)
    else:
        return None
def morris(root):
    current= root
    while current is not None:
        if current.left is None:
            print(current.data)
            current= current.right
        else:
            pre = current.left
            while pre.right is not None and pre.right !=current:
                pre=pre.right
            if pre.right is None:
                pre.right= current
                current= current.left
            else:
                pre.right=None
                print(current.data)
                current= current.right


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)
def inOrderPredeccessor(root):
    while root and root.right:
        root=root.right
    return root
def inOrderSuccessor(root):
    while root and root.left:
        root=root.left
    return root
def height(root):
    if not root:
        return 0
    x=height(root.left)
    y=height(root.right)
    return x+1 if x>y else y+1
def deleteNode(root, key):
    if not root:
        return None
    if not root.left and not root.right:
        del root
        return None
    if key<root.data:
        root.left=deleteNode(root.left, key)
    elif key>root.data:
        root.right=deleteNode(root.right, key)
    else:
        if height(root.left)>height(root.right):
            q=inOrderPredeccessor(root.left)
            root.data=q.data
            root.left=deleteNode(root.left, q.data)
        else:
            q=inOrderSuccessor(root.right)
            root.data=q.data
            root.right=deleteNode(root.right, q.data)
    return root
def search1(root, key):
    if not root:
        return None
    if root.data==key:
        return root
    if root.data< key:
        return search1(root.right, key)
    else:
        return search1(root.left, key)
def insert1(root, key):
    if not root:
        return Node(key)
    if root.data==key:
        return root
    elif root.data<key:
        root.right= insert1(root.right, key)
    else:
        root.left= insert1(root.left, key)
    return root


def populateInorderSuccesor(root, next):
    if root:
        populateInorderSuccesor(root.right, next)
        root.next=next
        next= root
        populateInorderSuccesor(root.left, next)

def searchInOrder(inOrder, key, start, end):
    for i in range(start, end+1):
        if inOrder[i]==key:
            return i
def treeFromPreorder(preorder, start, end, inorder=[]):
    if len(inorder)==0:
        inorder=sorted(preorder)
    if start> end:
        return None
    # print(treeFromPreorder.preIndex)
    root = Node(preorder[treeFromPreorder.preIndex])
    treeFromPreorder.preIndex+=1
   
    if start==end:
        return root
    splitIndex = searchInOrder(inorder, root.data, start, end)
    root.left= treeFromPreorder(preorder, start, splitIndex-1, inorder)
    root.right= treeFromPreorder(preorder, splitIndex+1,end, inorder)
    return root
def getInOrder(root, res):
    if root:
        getInOrder(root.left, res)
        res.append(root.data)
        getInOrder(root.right, res)
def inorderToBalanced(res, start, end):
    if start> end:
        return None
    mid= (start+end)//2
    root= Node(res[mid])
    if start==end:
        return root
    root.left= inorderToBalanced(res, start, mid-1)
    root.right= inorderToBalanced(res,mid+1, end)
    return root
def bstToBalancedBST(root):
    res=[]
    getInOrder(root, res)
    return inorderToBalanced(res, 0, len(res)-1)
# root= Node(1)
# rInsert(root, 2)
# rInsert(root, 3)
# rInsert(root, 4)
# rInsert(root,5)
# rInsert(root,6)
# rInsert(root, 7)
# preOrder(root)
# root = bstToBalancedBST(root)
# print('  ')
# preOrder(root)

def merge(a,b ,n,m):
    i=j=0
    c=[]
    while i< n and j<m:
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        elif a[i]>b[j]:
            c.append(b[j])
            j+=1
        else:
            c.append(a[i])
            i+=1
            j+=1
    while i< n:
        c.append(a[i])
        i+=1
    while j<m:
        c.append(b[j])
        j+=1
    return c
def inorderToBalanced2(res, start, end):
    if start> end:
        return None
    mid = (start+end)//2
    root = Node(res[mid])
    if start==end:
        return root
    root.left = inorderToBalanced2(res, start, mid-1)
    root.right= inorderToBalanced2(res, mid+1, end)
    return root

# merge two balanced bst
def twoToOneBalanced(root1, root2):
    res1=[]
    res2=[]
    getInOrder(root1, res1)
    getInOrder(root2, res2)
    n=len(res1)
    m=len(res2)
    res3= merge(res1, res2, n,m)
    l=len(res3)
    return inorderToBalanced2(res3, 0,l)


class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    res=[]
    i=0
    def getInorder(self, root):
        if root:
            self.getInorder(root.left)
            self.res.append(root.data)
            self.getInorder(root.right)
    def inorderToBST(self, root):
        if root:
            self.inorderToBST(root.left)
            root.data=self.res[self.i]
            self.i+=1
            self.inorderToBST(root.right)
    def binaryTreeToBST(self, root):
        # code here
        self.getInorder(root)
        self.res=sorted(self.res)
        self.inorderToBST(root)
        return root

# Median of BST with O(1) space
def countNodes(root):
    # by morris
    count=0
    current= root
    while current is not None:
        if current.left is None:
            count+=1
            current=current.right
        else:
            pre= current.left
            while pre.right is not None and pre.right !=current:
                pre=pre.right
            if pre.right is None:
                pre.right = current
                current= current.left
            else:
                pre.right=None
                count+=1
                current= current.right
    return count
def findMedian(root):
    count = countNodes(root)
    current= root
    currCount=0
    while current is not None:
        if current.left is None:
            currCount+=1
            if count %2 !=0 and currCount== (count+1)//2:
                return prev.data
            if count %2 ==0 and currCount== (count//2)+1:
                return (prev.data+current.data)//2
            prev= current
            current= current.right
        else:
            pre= current.left
            while pre.right is not None and pre.right != current:
                pre= pre.right

            if pre.right is None:
                pre.right= current
                current= current.left
            else:
                pre.right=None
                currCount+=1
                prev= pre
                if count %2 !=0 and currCount== (count+1)//2:
                    return current.data
                if count %2 ==0 and currCount== (count//2)+1:
                    return (prev.data+current.data)//2
                prev=current
                current= current.right
#  count in range
def getCount(root,low,high):
    ##Your code here
    current= root
    count=0
    while current is not None:
        if current.left is None:
            if current.data >=low and current.data<=high:
                count+=1
            current= current.right
        else:
            pre = current.left
            while pre.right is not None and pre.right!=current:
                pre= pre.right
            if pre.right==None:
                pre.right= current
                current= current.left
            else:
                pre.right=None
                if current.data >=low and current.data<=high:
                   count+=1
                current= current.right
    return count               

def insertSucc(node, data):
    global succ
    root=node
    if node==None:
        return Node(data)
    if data< node.data:
        succ=node
        root.left = insertSucc(node.left, data)
    elif data> node.data:
        root.right= insertSucc(node.right, data)
    return root

def replaceWithleastGreater(arr):
    n= len(arr)
    global succ
    root=None
    for i in range(n-1, -1 ,-1):
        succ=None
        root= insertSucc(root, arr[i])
        if succ:
            arr[i]= succ.data
        else:
            arr[i]=-1
    return arr

succ=None
print(replaceWithleastGreater([4,3,5,10,8]))
    
def checkDeadEnd(root, min , max):
    if not root:
        return False
    if min==max:
        return True
    return (checkDeadEnd(root.left, min, root.data-1) or checkDeadEnd(root.right, root.data+1, max))

# flatten BST and return root 
prev=None
def inorderBST(root):
    global prev
    if root:
        inorderBST(root.left)
        prev.right = root
        prev.left =None
        prev= root
        inorderBST(root.right)


def flatten(parent):
    global prev
    dummy = Node(-1)
    prev= dummy
    inorderBST(parent)
    prev.right=None
    prev.left=None
    return dummy.right


root=Node(50)
rInsert(root, 60)
rInsert(root, 80)
rInsert(root, 40)
rInsert(root,20)
rInsert(root,45)
rInsert(root, 55)


# inOrder(root) 
print(' ')
# morris(root)

# deleteNode(root, 50)
# deleteNode(root, 81)
# inOrder(root)

# treeFromPreorder.preIndex=0
# root=treeFromPreorder([10,5,1,7,40,50],0,5)
# inOrder(root)

# search(root, 80)

