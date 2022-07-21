
def smallestSumContigousArray(arr, n):
    min_sum_till_now= float('inf')
    sum=0
    for i in range(n):
        sum+=arr[i]
        if sum<min_sum_till_now:
            min_sum_till_now = sum
        if sum>0:
            sum=0
    return min_sum_till_now
print(smallestSumContigousArray([-1, -2, -3, -4],4))