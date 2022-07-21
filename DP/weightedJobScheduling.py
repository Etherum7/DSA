#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs=sorted(Jobs, key=lambda x : x.profit, reverse=True)
        dead=[0]*101
        res=0
        count=0
        for item in Jobs:
            if dead[item.deadline]==0:
                dead[item.deadline]=1
                res+=item.profit
                count+=1
            else:
                i=item.deadline-1
                while i>0 and dead[i]!=0:
                    i-=1
                if i!=0:
                    dead[i]=1
                    res+=item.profit
                    count+=1
        return [count,res]
        # code here