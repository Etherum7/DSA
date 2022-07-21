# do top down
# simple recursion 2 calls row col and ans exponential
# m*n
# ncr formulation
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = n+m-2
        R = m-1
        res = 1
        for i in range(1, R+1):
            res = res*(N-R+i)/i
        return int(res)


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num1 = num2 = -1
        c1 = c2 = 0
        for num in nums:
            if num == num1:
                c1 += 1
            elif num == num2:
                c2 += 1
            elif c1 == 0:
                num1 = num
                c1 += 1
            elif c2 == 0:
                num2 = num
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        c1 = c2 = 0
        for num in nums:
            if num == num1:
                c1 += 1
            elif num == num2:
                c2 += 1
        res = []
        if c1 > n//3:
            res.append(num1)
        if c2 > n//3:
            res.append(num2)
        return res
