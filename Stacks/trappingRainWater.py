class Solution:
    def trappingWater(self, arr,n):
        mxL=[0]*n
        mxR=[0]*n
        mxL[0]=arr[0]
        mxR[n-1]=arr[n-1]
        t=mxL[0]
        for i in range(1,n):
            mxL[i]= max(t, arr[i])
            t=mxL[i]
        
        t=mxR[n-1]
        for i in range(n-2, -1, -1):
            mxR[i]= max(t, arr[i])
            t=mxR[i]
        res=[0]*n
        for i in range(n):
            res[i]=min(mxL[i], mxR[i])-arr[i]
        return sum(res)