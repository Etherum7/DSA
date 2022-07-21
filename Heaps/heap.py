import sys
import heapq

class Node():
    def __init__(self,data=0):
        self.data=data
        self.right=None
        self.left=None

class Heap:
    def __init__(self, maxsize):
        self.maxsize=maxsize
        self.size=0
        self.Heap=[0]*(self.maxsize+1)
        self.front=1
        self.Heap[0]=sys.maxsize
    def parent(self, pos):
        return pos//2
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos],self.Heap[fpos]
    def insert(self, key):
        if self.size> self.maxsize:
            return
        self.size+=1
        self.Heap[self.size]=key
        current=self.size
        while self.Heap[current]> self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current=self.parent(current)

    
def insertHeap(array, i):
    while i>0 and  array[(i-1)//2]< array[i]:
        array[(i-1)//2], array[i] = array[i], array[(i-1)//2]
        i=(i-1)//2
    
def createHeapFromArray(array):
    for i in range(1 , len(array)):
        insertHeap(array, i)
def heapify(array, n):
    for i in range((n//2)-1, -1, -1):
        j=(2*i)+1
        while (j< n-1):
            if (array[j+1]> array[j]):
                j=j+1
            if array[j]> array[i]:
                array[i], array[j] = array[j], array[i]
                i=j
                j=(2*i)+1
            else:
                break
def deleteHeapFromArray(array,n):
    x=array[0]
    i=0
    j=1
    array[0]=array[n-1]
    while(j< n-1):
        if ( array[j+1]> array[j]):
            j=j+1
        if array[j]> array[i]:
            array[i], array[j]=array[j], array[i]
            i=j
            j=(2*i)+1
        else :
            break;
    array[n-1]=x
def heapSort(array):
    n= len(array)
    createHeapFromArray(array)
    for i in range(n):
        deleteHeapFromArray(array, n-i)
# max subarray contigous
from heapq import heapify, heappush, heappop
class Solution:
    def max_of_subarrays(self,arr,n,k):
        '''
        you can use collections module here.
        :param a: given array
        :param n: size of array
        :param k: value of k
        :return: A list of required values 
        '''
        i=0
        res=[]
        arr=[-1 * i for i in arr]
        while (n-i>=k):
            heap=arr[i: i+k]
            heapify(heap)
            res.append(-1 * heap[0])
            i+=1
        return res
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        heapq.heapify(arr)
        res=[]
        for i in range(0,k-1):
            heapq.heappop(arr)
        return heapq.heappop(arr)

    def kthLargestContigoiosSubArraySum(arr,k):
        # make array
        sum=[0]
        n=len(arr)
        sum.append(arr[0])
        for i in range(2, n+1):
            sum.append(arr[i-1]-sum[i-1])
        Q=[]
        heapq.heapify(Q)
        for i in range(1, n+1):
            for j in range(i, n+1):
                x=sum[j]-sum[i-1]
                if len(Q)<k:
                    heapq.heappush(Q,x)
                elif Q[0]<x:
                    heapq.heapush(x)
                    heapq.heappop(Q)
        return Q[0]
# Reorganize strings
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        d={}
        for i in s:
            if not i in  d:
                d[i]=1
            else: 
                d[i]+=1
        Q=[]
        res=''
        prev=''
        freq=0
        heapq.heapify(Q)
        for (key, value) in d.items():
            heapq.heappush(Q, (-1 * value, key))
            
        while len(Q):
            

            t= heapq.heappop(Q)
            res+=t[1]
            if freq<0 and prev:
                heapq.heappush(Q, (freq, prev))
            freq=t[0]+1
            prev=t[1]
        if len(res) !=len(s):
            return ''
        return res
def getInOrder(root, res):
    if root:
         getInOrder(root.left, res)
         res.append(root.data)
         getInOrder(root.right, res)
def convertBSTToMinHeap(root, res , ind):
    if not root:
        return
    ind[0]+=1
    root.data=res[ind[0]]
    convertBSTToMinHeap(root.left, res, ind)
    convertBSTToMinHeap(root.right, res, ind)
def bstToMinHeap(root):
    res=[]
    ind=[-1]
    getInOrder(root, res)
    convertBSTToMinHeap(root, res, ind)
    preOrder(root)
def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)
root=Node(4)
root.left=Node(2)
root.right=Node(6)
root.left.left=Node(1)
root.left.right=Node(3)

root.right.left=Node(5)
root.right.right=Node(7)

bstToMinHeap(root)

# is heap
class Solution:
    #Your Function Should return True/False
    def count_nodes(self, root):
        if not root:
            return 0
        return 1+ self.count_nodes(root.left) + self.count_nodes(root.right)
    def isHeapUtil(self, root):
        if not root.right and not root.left:
            return True
        if not root.right:
            return root.data>= root.left.data
        if root.data>= root.left.data and root.data>=root.right.data:
            return self.isHeapUtil(root.left) and self.isHeapUtil(root.right)
        else:
            return False
        
    def isComplete(self, root, index, total):
        if not root:
            return True
        if index> total:
            return False
        return self.isComplete(root.left, (2*index)+1, total ) and self.isComplete(root.right, (2*index)+2, total)

    def isHeap(self, root):
        total=self.count_nodes(root)
        if self.isComplete(root, 0, total):
            return self.isHeapUtil(root)
        return False

# minheap to maxheap to
def minHeapToMaxHeap(arr):
    n=len(arr)
    for i in range((n//2)-1, -1, -1):
        j=(2*i)+1
        while j< n-1:
            if arr[j]<arr[j+1]:
                j=j+1
            if arr[j]> arr[i]:
                arr[i], arr[j]=arr[j],arr[i]
                i=j
                j=(2*i)+1
# min sum digits sum
def solve(self, arr, n):
        heapq.heapify(arr)
        x1=0
        x2=0
        while len(arr):
            x1=x1*10+heapq.heappop(arr)
            if len(arr):
               x2=x2*10+heapq.heappop(arr)
        return x1+x2


A=[10,8,20,5,12,6, 7]
# heapSort(A)
# heapify(A, len(A))
# print(A)
