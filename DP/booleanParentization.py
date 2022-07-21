#User function Template for python3

class Solution:
    def __init__(self):
        self.t={}
    def convert(self, i, j, isTrue):
        return str(i)+" "+ str(j)+ " "+ str(isTrue)
    def util(self, S, i , j, isTrue):
        if i>j:
            return 0
        if i==j:
            if isTrue:
                return 1 if S[i]=="T" else 0
            else:
                return 1 if S[i]=="F" else 0
        key=self.convert(i, j, isTrue)
        if key in self.t:
            return self.t[key]
        ans=0
        for k in range(i+1, j,2):
            lTKey=self.convert(i, k-1, 1)
            rTKey=self.convert(k+1, j,1)
            lFKey= self.convert(i, k-1, 0)
            rFKey= self.convert(k+1, j, 0)
            if lTKey in self.t:
                lT=self.t[lTKey]
            else:
                lT= self.util(S,i, k-1, 1)
                
            if rTKey in self.t:
                rT=self.t[rTKey]
            else:
                rT= self.util(S,k+1, j, 1)
            
            if rFKey in self.t:
                rF=self.t[rFKey]
            else:
                rF= self.util(S,k+1, j, 0)
              
            if lFKey in self.t:
                lF=self.t[lFKey]
            else:
                lF= self.util(S,i, k-1,0)
                
            if S[k]=='&':
                if isTrue:
                    ans=ans+lT*rT
                else:
                    ans=ans+(lT*rF) +( lF*rT) + (lF*rF)
            elif S[k]=='|':
                if isTrue:
                    ans=ans+(lT*rT) + (lT*rF) +( lF*rT)
                else:
                    ans=ans+ (lF*rF)
            elif S[k]=='^':
                if isTrue:
                    ans=ans+ (lT*rF) +( lF*rT)
                else:
                    ans= ans+ (lF*rF)+ (lT*rT) 
            self.t[key]=ans
        return ans%1003
    def countWays(self, N, S):
        # code here
        return self.util(S, 0, N-1, True)
ob=Solution()
ob.countWays('')