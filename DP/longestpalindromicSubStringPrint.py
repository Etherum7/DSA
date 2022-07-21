#User function Template for python3
class Solution:
    def longestPalin(self, S):
        # code here
        n=len(S)
        
        t=[[False for i in range(n)] for j in range(n)]
        i=0
        maxLeft=0
        maxRight=0
        while i<n:
            t[i][i]=True
            i+=1
        maxLength=1
        
        i=0
        while i< n-1:
            if S[i]==S[i+1]:
                t[i][i+1]=True
                maxLength=2
                maxLeft=i
                maxRight=i+1
            i+=1
        k=3
        while k<= n:
            i=0
            while i<n-k+1:
                j=i+k-1
                if t[i+1][j-1] and S[i]==S[j]:
                    t[i][j]=True
                    if k>maxLength:
                        maxLength=k
                        maxLeft=i
                        maxRight=j
                i+=1
            k+=1
        print(maxLeft, maxRight)
        return S[maxLeft: maxRight+1]
ob=Solution()
print(ob.longestPalin('rfkqyuqfjkxy'))
#User function Template for python3

class Solution:
    def longestPalin(self, string):
        # code here
         n = len(string) # calculating size of string
         if (n < 2):
             
             return string[0] # if string is empty then size will be 0.
                  # if n==1 then, answer will be 1(single
                  # character will always palindrome)
         start=0
         maxLength = 1
         for i in range(n):
             low = i - 1
             high = i + 1
             while (high < n and string[high] == string[i] ):                              
                 high=high+1
       
             while (low >= 0 and string[low] == string[i] ):                
                 low=low-1
       
             while (low >= 0 and high < n and string[low] == string[high] ):
               low=low-1
               high=high+1
         
     
             length = high - low - 1
             if (maxLength < length):
                 maxLength = length
                 start=low+1
             
         
         return string[start:start + maxLength]