# User function Template for python3
from heapq import heappush, heappop


class Solution:
    def kthLargest(self, k, arr, n):
        # code here
        res = []
        heap = []
        for i in range(n):
            if i < k-1:
                res.append(-1)
                heappush(heap, arr[i])

            elif i == k-1:
                heappush(heap, arr[i])
                res.append(heap[0])
            else:

                if heap[0] < arr[i]:
                    heappop(heap)
                    heappush(heap, arr[i])
                res.append(heap[0])
        return res
