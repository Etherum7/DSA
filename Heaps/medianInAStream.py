from heapq import heappush, heappop


class Solution:
    # def balanceHeaps(self):
    # Balance the two heaps size , such that difference is not more than one.
    # code here

    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def getMedian(self):
        # return the median of the data received till now.
        # code here
        if len(self.min_heap) != len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0]-self.max_heap[0])/2

    def insertHeaps(self, x):
        #:param x: value to be inserted
        #:return: None
        # code here
        heappush(self.max_heap, -x)
        heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
