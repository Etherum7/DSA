# Moore voting n/2
class Solution:
    def majorityElement(self, A, N):
        # Your code here
        count = 0
        candidiate = 0
        for num in A:
            if count == 0:
                candidiate = num
            if num == candidiate:
                count += 1
            else:
                count -= 1
        count = 0
        for num in A:
            if num == candidiate:
                count += 1
        if count > len(A)//2:
            return candidiate
        return -1

# n/3


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
