class Solution:
    def overlappedInterval(self, Intervals):
        #Code here
        st=[]
        Intervals=sorted(Intervals, key=lambda x: x[0])
        st.append(Intervals[0])
        for i in range(1, len(Intervals)):
          #  print(Intervals)
            cur=Intervals[i]
            top=st[-1]
            if top[1]<cur[0]:
                st.append(cur)
            elif top[1]<cur[1]:
                top[1]=cur[1]
                st.pop()
                st.append(top)
          
        return st

#{ 
#  Driver Code Starts
        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().strip().split()))
        Intervals = []
        j = 0
        for i in range(n):
            x = a[j]
            j += 1
            y = a[j]
            j += 1
            Intervals.append([x,y])
        obj = Solution()
        ans = obj.overlappedInterval(Intervals)
        for i in ans:
            for j in i:
                print(j, end = " ")
        print()
# } Driver Code Ends