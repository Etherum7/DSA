class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        for j in range(1,n):
            if nums[j]==nums[j-1]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
        return i+1