#User function Template for python3
#User function Template for python3
from heapq import heappush, heappop
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        heap=[]
        op=[]
        n=len(arr)
        for i in range(K):
            heappush(heap, (arr[i][0],i, 1))
        while len(heap):
            temp=heappop(heap)
            op.append(temp[0])
            if temp[2]!=K:
                heappush(heap, (arr[temp[1]][temp[2]],temp[1], temp[2]+1))
        return op

class Solution:
    #Function to merge k sorted arrays.
    def merge(self,arr1, arr2):
        n=len(arr1)
        m=len(arr2)
        arr3=[]
        i=0
        j=0
        while i< n and j< m:
            if arr1[i]<arr2[j]:
                arr3.append(arr1[i])
                i+=1
            elif arr1[i]>arr2[j]:
                arr3.append(arr2[j])
                j+=1
            else:
                arr3.append(arr1[i])
                arr3.append(arr1[i])
                i+=1
                j+=1
        while i< n:
            arr3.append(arr1[i])
            i+=1
        while j<m:
            arr3.append(arr2[j])
            
            j+=1
        return arr3
        
    def mergeKArrays(self, arr, K):
        if K==1:
            return arr[0]
        elif K==2:
            
            return self.merge(arr[0], arr[1])
        elif K>2:
          if K%2==0:
              split=K//2
              arr1=self.mergeKArrays(arr[:split],K-split)
              arr2=self.mergeKArrays(arr[split:], split)
          else:
              split=K//2
              arr1=self.mergeKArrays(arr[:split+1],K-split)
              arr2=self.mergeKArrays(arr[split+1:], split)
        return self.merge(arr1, arr2)