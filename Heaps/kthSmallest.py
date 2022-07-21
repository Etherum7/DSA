from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        heap = []
        for i in range(k):
            heappush(heap, -arr[i])
        for i in range(k, r+1):
            if abs(heap[0]) > arr[i]:
                heappop(heap)
                heappush(heap, -arr[i])
        return -heappop(heap)
