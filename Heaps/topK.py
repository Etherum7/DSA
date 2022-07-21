# bad
# nlarget method
# import heapq
from heapq import heappush, heappop
from heapq import heappush, heappop, heapify


class Solution:
    def topK(self, nums, k):
        # Code here
        mp = dict()
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        heap = [(-value, key) for key, value in mp.items()]
        heapify(heap)
# 		kLargest=heapq.nlargest(k, heap)

        op = []
# 		print(heap)
        while len(heap) and len(op) != k:
            heap2 = []
            t = heappop(heap)
            heappush(heap2, -t[1])
            while len(heap) and t[0] == heap[0][0]:

                heappush(heap2, -heappop(heap)[1])

            while len(op) < k and len(heap2):
                op.append(-heappop(heap2))
        return op


class Solution:
    def topK(self, nums, k):
        # Code here
        heap = []
        nums.sort()
        n = len(nums)
        cnt = 1
        num = nums[0]

        for i in range(1, n):
            if nums[i] == num:
                cnt += 1

            else:
                heappush(heap, (-cnt, num))
                cnt = 1
                num = nums[i]
        heappush(heap, (-cnt, num))
# 		print(heap)
        op = []
        while len(op) != k:
            t = heappop(heap)
            heap2 = []
            heappush(heap2, t[1])
            while len(heap) and heap[0][0] == t[0]:
                heappush(heap2, t[1])
            while len(op) < k+1 and len(heap2):
                op.append(heappop(heap2))
        return op
