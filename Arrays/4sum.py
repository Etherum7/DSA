class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        i=0
        while i<n:
            j=i+1
            while j<n-1:
                u=j+1
                v=n-1
                while u<v:
                    if nums[i]+nums[j]+nums[u]+nums[v]==target:
                        quadruple=[0]*4
                        quadruple[0]=nums[i]
                        quadruple[1]=nums[j]
                        quadruple[2]=nums[u]
                        quadruple[3]=nums[v]
                        res.append(quadruple)
                        temp1=nums[u]
                        temp2=nums[v]
                        while u<v and temp1==nums[u]:
                            u+=1
                        while v>u and temp2==nums[v]:
                            v-=1
                    elif nums[i]+nums[j]+nums[u]+nums[v]<target:
                        u+=1
                    else:
                        v-=1
                temp1=nums[j]
                while j<n and temp1==nums[j]:
                    j+=1
            temp1=nums[i]
            while i<n and temp1==nums[i]:
                i+=1
        return res