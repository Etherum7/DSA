# User function Template for python3

class Solution:
    def util(self, ip, N, res, op, used):
        if len(op) == N:
            res.append(op)
            return
        for i in range( N):
            if i != 0 and (not used[i-1] and ip[i] == ip[i-1]) :
                continue
            if not used[i]:
                used[i] = True
                self.util( ip, N, res, op+ip[i], used)
                used[i] = False

    def find_permutation(self, S):
        # Code here
        res = []
        ip = list(S)
        ip.sort()
        used = [False]*len(ip)
        self.util( ip, len(ip), res, '', used)
        return res
ob=Solution()
print(ob.find_permutation('ABC'))

class Solution:
    def util(self, nums,pos, N,res):
        if pos==N:
            res.append(nums.copy())
            return
        for i in range(pos, N):
            nums[i],nums[pos]=nums[pos],nums[i]
            self.util(nums, pos+1, N, res)
            nums[i],nums[pos]=nums[pos],nums[i]
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        N=len(nums)
        self.util(nums, 0, N,res)
        return res