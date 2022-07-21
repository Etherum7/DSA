from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)
        for i in range(k):
            heappush(heap, nums[i])
        for i in range(k, n):
            if heap[0] < nums[i]:
                heappop(heap)
                heappush(heap, nums[i])
        return heappop(heap)
