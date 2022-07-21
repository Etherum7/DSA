class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        t=[[0 for i in range(y+1)] for j in range(2)]
        bi=bool
        for i in range( x+1):
            for j in range( y+1):
                bi=i&1
                if i==0 or j==0:
                    t[bi][j]=0
                
                    
                elif s1[i-1]==s2[j-1]:
                    t[bi][j]=1+t[1-bi][j-1]
                else:
                    t[bi][j]= max(t[1-bi][j] , t[bi][j-1])
        return t[bi][y]