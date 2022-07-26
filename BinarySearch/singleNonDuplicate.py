# O(n)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
