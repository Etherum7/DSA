#User function Template for python3

class Solution:
    def FirstNonRepeating(self, stream):
        # Code here
        res=''
        Max_size=256
        DLL=[]*Max_size
        repeated=[False]*Max_size
        for c in stream:
            if not repeated[ord(c)]:
                if not c in DLL:
                    DLL.append(c)
                    
                else:
                    DLL.remove(c)
                    repeated[ord(c)]=True
                    
            if len(DLL):
                res+=DLL[0]
            else:
                res+='#'
        return res
                
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)

# } Driver Code Ends