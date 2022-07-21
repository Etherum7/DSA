import math


# def maxSumSubArray0(A: list):
#     # brute force
#     max = -math.inf
#     max_left = 0
#     max_right = 0
#     for i, elem1 in enumerate(A):
#         sum = elem1
#         if(sum > max):
#             max = sum
#             max_left = i
#             max_right = i
#         for j, elem2 in enumerate(A[i+1:]):
#             sum += elem2
#             if(sum > max):
#                 max = sum
#                 max_left = i
#                 max_right = j+i+1
#     return (max_left, max_right, max)


def maxCrossingSubArray(A, low, mid, high):
    leftSum = -math.inf
    sum = 0
    maxLeft = maxRight = mid
    for i in range(mid, low+1, -1):
        sum += A[i]
        if(sum > leftSum):
            leftSum = sum
            maxLeft = i

    rightSum = -math.inf
    sum = 0
    for i in range(mid+1, high+1):
        sum += A[i]
        if(sum > rightSum):
            rightSum = sum
            maxRight = i
    return (maxLeft, maxRight, leftSum+rightSum)

    
def maxSubArray(A: list, low, high):

    # divide and conquer O(nlogn)
    if(low == high):
        return (low, high, A[low])
    else:
        mid = math.floor((low+high)/2)
        (leftLow, leftHigh, leftSum) = maxSubArray(A, low, mid)
        (rightLow, rightHigh, rightSum) = maxSubArray(A, mid+1, high)
        (crossLow, crossHigh, crossSum) = maxCrossingSubArray(A, low, mid, high)
        if(leftSum >= rightSum and leftSum >= crossSum):
            return (leftLow, leftHigh, leftSum)
        elif(rightSum >= leftSum and rightSum >= crossSum):
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)


# print(maxSubArray([0, 13, -3, -25, 20, -3, -16, -23, 18,
#                    20, -7, 12, -5, -22, 15, -4, 7], 0, 16))
print(maxSubArray([-10, -4, -7], 0, 2))
# print(maxSubArray([12]))


def maxSubArray2(A: list):
    maxLeft = maxRight = 0
    maxSum = -math.inf
    sum = 0
    for i, elem in enumerate(A):
        sum += elem
        tempSum = sum
        for j in range(0, i):
            tempSum -= A[j]
            if(tempSum > maxSum):
                maxSum = tempSum
                maxLeft = j+1
                maxRight = i

    return (maxLeft, maxRight, maxSum)

print(maxSubArray([10, -4, -7], 0, 2))

print(maxSubArray2([0, 13, -3, -25, 20, -3, -16, -23, 18,
                   20, -7, 12, -5, -22, 15, -4, 7]))


# import math
# class Solution:
#     def maxCrosssingSubArray(self, A, low, mid, high):
#         leftSum=0
#         i=mid
#         sum=0
#         while(i>=low):
#             sum+=A[i]
#             if(sum>leftSum):
#                 leftSum= sum
                
#             i-=1
#         rightSum=0
#         sum=0
#         j=mid+1
#         while(j<high):
            
#             sum+=A[j]
#             if(sum>rightSum):
#                 rightSum= sum
                
#             j+=1
#         return  leftSum+rightSum
        
        
#     ##Complete this function
#     #Function to find the sum of contiguous subarray with maximum sum.
#     def maxSubArraySum(self,A,size, low=0):
#         ##Your code here
#         if(low==size):
#             return A[low-1]
        
#         mid=math.floor((low+size-1)/2)
#         leftSum= self.maxSubArraySum(A, mid,low)
#         rightSum= self.maxSubArraySum(A, size,mid+1)
#         crossSum= self.maxCrosssingSubArray(A,low,  mid,size)
        
#         if(leftSum>rightSum and leftSum> crossSum):
#             return leftSum
#         elif(rightSum>leftSum and  rightSum>crossSum):
#             return rightSum
#         else:
#             return crossSum
# soln = Solution()

# print(soln.maxSubArraySum([0, 13, -3, -25, 20, -3, -16, -23, 18,
#                    20, -7, 12, -5, -22, 15, -4, 7], 17))
