class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            j = i+1
            k = n-1
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                while j < k:
                    cur = nums[j]+nums[k]+nums[i]
                    if cur == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif cur > 0:
                        k -= 1
                    else:
                        j += 1
        return res
