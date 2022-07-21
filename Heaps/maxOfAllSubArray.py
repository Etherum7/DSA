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