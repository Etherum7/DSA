#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        i=0
        j=n-1
        while i<j:
            if M[i][j]==1:
                i+=1
            else:
                j-=1
        candidate=i
        c1=0
        c2=0
        for i in range(n):
            
            c1+=M[i][candidate]
            c2+=M[candidate][i]
        if c1==n-1 and c2==0:
            return candidate
        return -1
def celebrityStack(self, M, n):
        # code here 
        st=[i for i in range(n)]
        while len(st)>1:
            p1=st.pop()
            p2=st.pop()
            if M[p1][p2]==1:
                st.append(p2)
            else:
                st.append(p1)
        if len(st)==1:
            c1=c2=0
            for i in range(n):
                if i!=st[0]:
                    c1+=M[st[0]][i]
                    c2+=M[i][st[0]]
            if c1==0 and c2==n-1:
                return st[0]
        return -1
def celebrityBF(M, n):
    # code here
    t = []
    for i in range(n):
        if sum(M[i]) == 0:
            t.append(i)
    if not len(t):
        return -1
    res = []
    for col in t:
        flag = 1
        for row in range(n):
            if row == col and M[row][col] == 0:
                continue
            if M[row][col] != 1:
                flag = 0
        if flag:
            return col
    return -1


def celebrityGraph(M, n):
    # code here
    ind = [0]*n
    outd = [0]*n
    for row in range(n):
        for col in range(n):
            if M[row][col] == 1:
                ind[col] += 1
                outd[row] += 1
    for i, val in enumerate(ind):
        if val == n-1 and outd[i] == 0:
            return i
    return -1

class Solution:
    def util(self, curr , M):
        if curr==0:
            return 0
        t=self.util(curr-1,M)
        if t==-1:
            for i in range(curr):
                if M[curr][i]!=0:
                    return -1
            for j in range(curr):
                if M[j][curr]!=1:
                    return -1
            return curr
                
        if  M[t][curr]==1 and M[curr][t]==0:
            return curr
        
        elif M[t][curr]==0 and M[curr][t]==1:
            return t
        else:
            return -1
            
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        return self.util(n-1, M)
         


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends

ob=Solution()
