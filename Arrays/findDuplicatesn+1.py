class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# if only two times repeated
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # HT={}
        # for i in nums:
        #     if not i in HT:
        #         HT[i]=1
        #     else:
        #         return i
        n = len(nums)
        sumNow = sum(nums)
        sumShouldBe = 0
        for i in range(1, n):
            sumShouldBe += i
        return sumNow-sumShouldBe
