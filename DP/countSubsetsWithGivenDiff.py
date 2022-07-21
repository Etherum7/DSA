def countSubsetSum(arr,n,s1):
    t=[[1 if i==0 and j==0 else 0 for i in range(s1+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, s1+1):
            if arr[i-1]>j:
                t[i][j]=t[i-1][j]
            elif arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j]
    return t[n][s1]
def countSubsetsWithGivenDiff(arr,n, diff):
    r=sum(arr)
    s1=(r+diff)/2
    print(s1)
    return countSubsetSum(arr, n, s1)
arr=[1,1,2,3]
diff=1
n=4
print(countSubsetsWithGivenDiff(arr, n, diff))