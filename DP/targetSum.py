class Solution:
    def countSubsetSum(self, arr, n, s):
        t=[[1 if i==j==0 else 0 for i in range(s+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(0, s+1):
                if arr[i-1]>j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]= t[i-1][j-arr[i-1]] + t[i-1][j]
        return t[n][s]
                
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        r=sum(nums)
        if (r+target)%2 !=0:
            return 0
        s1=(r+target)//2
        return self.countSubsetSum(nums, len(nums), abs(s1))