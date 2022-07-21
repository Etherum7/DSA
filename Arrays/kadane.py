class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSumTillNow=0
        maxSum=-float('inf')
        for i in range(len(nums)):
            maxSumTillNow+=nums[i]
            if maxSum<maxSumTillNow:
                maxSum=maxSumTillNow
            if maxSumTillNow<0:
                maxSumTillNow=0
        return maxSum