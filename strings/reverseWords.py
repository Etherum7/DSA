class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        n=len(S)
        j=n
        ans=''
        for i in range(n-1, -1, -1):
            if S[i]=='.':
                ans+=S[i+1: j]
                ans+='.'
                j=i
        # print(i,j)
        ans+=S[i: j]
        return ans
# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        st=[]
        j=0
        for i in range(len(S)):
            if S[i] == '.':
                st.append(S[j:i])
                j = i+1
        st.append(S[j:i+1])
        ans=''
        while len(st):
            ans+=st.pop()
            ans+='.'
        return ans[:-1]
class Solution:

    # Function to reverse words in a given string.
    def reverseWords(self, S):
        # code here
        arr = []
        j = 0
        for i in range(len(S)):
            if S[i] == '.':
                arr.append(S[j:i])
                j = i+1
        arr.append(S[j:i+1])
        arr = arr[::-1]
        return '.'.join(arr)
