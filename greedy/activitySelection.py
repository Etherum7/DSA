class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        activities=[(start[i],end[i]) for i in range(n)]
        activities.sort(key=lambda x:x[1])
        cnt=0
        last=(0,0)
        i=0
        while i<n:
            if last[1]<activities[i][0]:
                cnt+=1
                last=activities[i]
            i+=1
        return cnt