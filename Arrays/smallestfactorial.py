# User function Template for python3

class Solution:
    def check(self, num, n):
        f = 5
        temp = 0

        while f <= num:
            temp += num//f
            f *= 5
        return temp >= n

    def findNum(self, n: int):
        # Complete this function
        if n == 1:
            return 5
        low = 0
        high = 5*n
        while low < high:
            mid = (low+high) >> 1
            if self.check(mid, n):
                high = mid
            else:
                low = mid+1
        return low
