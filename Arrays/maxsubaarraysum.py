import math
def maxSubArraySum(A):
    max_sum=-math.inf
    max_sum_till_now=0
    for i in range(len(A)):
        max_sum_till_now=max_sum_till_now+A[i]
        # print(max_sum_till_now)
        if(max_sum_till_now>max_sum):
            max_sum=max_sum_till_now
        if(max_sum_till_now<0):
            max_sum_till_now=0
    return max_sum
print(maxSubArraySum([1,2,3,-4,9]))


