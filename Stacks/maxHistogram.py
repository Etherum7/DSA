class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        #code here
        nsl=[]
        st1=[]
        nsr=[]
        st2=[]
        n=len(histogram)
        for i in range(n):
            while len(st1) and st1[-1][0]>histogram[i]:
                st1.pop()
            if len(st1)==0:
                nsl.append(-1)
            else:
                nsl.append(st1[-1][1])
            st1.append((histogram[i], i))
        for i in range(n-1, -1, -1):
            while len(st2) and st2[-1][0]>histogram[i]:
                st2.pop()
            if len(st2)==0:
                nsr.append(-1)
            else:
                nsr.append(st2[-1][1])
            st2.append((histogram[i], i))
        nsr=nsr[::-1]
        print(nsl, nsr)
        res=[0]*n
        for i in range(n):
            if nsr[i]==-1:
                nsr[i]=n
            if nsl[i]==-1:
                nsl[i]=0
                
                res[i]=histogram[i]*(nsr[i]-nsl[i])
            else:
                res[i]=histogram[i]*(nsr[i]-nsl[i]-1)
            print(nsl[i],nsr[i])
        print(res)
        return max(res)
ob=Solution()
# print(ob.getMaxArea([6 ,2 ,5 ,4 ,5 ,1 ,6]))
print(ob.getMaxArea([5,4,3,2,1]))