def long_subarray(arr, k,n):
    i=j=0
    mx=0
    s=0
    while j< n:
        s+=arr[j]
        if s<k:
            j+=1
        elif s==k:
            mx=max(mx, j-i+1)
            j+=1
        elif s>k:
            while s>k:
                s-=arr[i]
                i+=1
                if s==k:
                    mx=max(mx, j-i+1)
            j+=1
    return mx
# print(long_subarray([4,1,1,1,2,3,5], 5, 7))
# print(long_subarray([1,2,3,7,5], 12, 5))
# 0sum
class Solution:
    def maxLen(self, n, arr):
        #Code here
        d={}
        maxLen=0
        cummulativeSum=0
        for i in range(len(arr)):
            cummulativeSum+=arr[i]
            if cummulativeSum==0:
                maxLen=i+1
            elif cummulativeSum in d:
                maxLen=max(maxLen, i-d[cummulativeSum])
            if cummulativeSum not in d:
                d[cummulativeSum]=i
        return maxLen
            
def long_subarray_neg(arr,n,k):
    d={}
    s=0
    maxLen=0
    for i in range(n):
        s+=arr[i]
        if s==k:
            maxLen=i+1
        elif s-k in d:
            maxLen= max(maxLen,i-d[s-k])
        if not s in d:
            d[s]=i
    return maxLen
print(long_subarray_neg([-5, 8, -14, 2, 4, 12],6,-5))
print(long_subarray_neg([10, 5, 2, 7, 1, 9],6,15))