#User function Template for python3
# Optimize
class Solution:
    def say(self,s):
        res=''
        i=0
        N=len(s)
        while i<N:
            cnt=1
            while i+1< N and s[i]==s[i+1]:
                cnt+=1
                i+=1
            res+=str(cnt)+s[i]
            i+=1
        return res

    def lookandsay(self, n):
        # code here
        if n==1:
            return '1'
        res='1'
        for i in range(n-1):
            # print(res)
            res=self.say(res)
        return res