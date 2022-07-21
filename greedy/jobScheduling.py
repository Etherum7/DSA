from typing import List

#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        sz=0
        for i in range(n):
            sz=max(sz, Jobs[i].deadline)
        deadlines=[0]*(sz+1)
        profit=0
        cnt=0
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        for job in Jobs:
            deadline=job.deadline
            for i in range(deadline,0,-1 ):
                if deadlines[i]==0:
                    deadlines[i]=job.profit
                    profit+=job.profit
                    cnt+=1
                    break
        return [cnt,profit]

def JobScheduling(Jobs ,n):
        Jobs.sort( key=lambda x: x[1], reverse=True )
        print(Jobs)
        res=[0]*n
        Jobs.sort( key=lambda x: x[2], reverse=True )
        for i in range(len(Jobs)):
            if(res[Jobs[i][1]]==0):
                res[Jobs[i][1]]=Jobs[i][2]
            else:
                t=Jobs[i][1]-1
                while (t>0 and res[t]!=0):
                    t-=1
                if(t>0):
                    res[t]=Jobs[i][2]
        print(res)



        print(Jobs)
JobScheduling([[1,2,100],[2,1,19],[3,2,27],[4,1,25],[5,1,15]], 5)
# Program to find the maximum profit
# job sequence from a given array
# of jobs with deadlines and profits
# import heapq


# def printJobScheduling(arr):
# n = len(arr)

# # arr[i][0] = job_id, arr[i][1] = deadline, arr[i][2] = profit

# # sorting the array on the
# # basis of their deadlines
# arr.sort(key=lambda x: x[1])

# # initialise the result array and maxHeap
# result = []
# maxHeap = []

# # starting the iteration from the end
# for i in range(n - 1, -1, -1):

# # calculate slots between two deadlines
# if i == 0:
# slots_available = arr[i][1]
# else:
# slots_available = arr[i][1] - arr[i - 1][1]

# # include the profit of job(as priority), deadline
# # and job_id in maxHeap
# # note we push negative value in maxHeap to convert
# # min heap to max heap in python
# heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))

# while slots_available and maxHeap:

# # get the job with max_profit
# profit, deadline, job_id = heapq.heappop(maxHeap)

# # reduce the slots
# slots_available -= 1

# # include the job in the result array
# result.append([job_id, deadline])

# # jobs included might be shuffled
# # sort the result array by their deadlines
# result.sort(key=lambda x: x[1])

# for job in result:
# print(job[0], end=" ")
# print()


# # Driver COde
# arr = [['a', 2, 100], # Job Array
# ['b', 1, 19],
# ['c', 2, 27],
# ['d', 1, 25],
# ['e', 3, 15]]

# print("Following is maximum profit sequence of jobs")

# # Function Call
# printJobScheduling(arr)

# # This code is contributed
# # by Shivam Bhagat
