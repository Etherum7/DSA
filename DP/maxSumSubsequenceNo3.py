def maxSumSSNo3(arr ,n):
    sum=[0]*n
    if n >= 1 :
        sum[0] = arr[0]
     
    if n >= 2 :
        sum[1] = arr[0] + arr[1]
     
    if n > 2 :
        sum[2] = max(sum[1], max(arr[1] + arr[2], arr[0] + arr[2]))
    for i in range(3, n):
        sum[i]= max(sum[i-1], sum[i-2]+arr[i], sum[i-3]+arr[i]+arr[i-1])
    return sum[n-1]
print(maxSumSSNo3([3000, 2000, 1000, 3, 10],5))
print(maxSumSSNo3([100, 1000, 100, 1000, 1],5))
print(maxSumSSNo3([1, 1, 1, 1, 1],5))
print(maxSumSSNo3([1, 2, 3, 4, 5, 6, 7, 8],8))