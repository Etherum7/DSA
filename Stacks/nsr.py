#User function Template for python3

class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        st=[]
        res=[]
        for i in range(n-1, -1, -1):
            while len(st) and st[-1]>=arr[i]:
                st.pop()
            if len(st)==0:
                res.append(-1)
            else:
                res.append(st[-1])
            st.append(arr[i])
        return res[::-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

# } Driver Code Ends