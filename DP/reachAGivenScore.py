def count(n):
    #your code here
    arr=[3,5,10]
    t=[[ 1 if i==0 else 0 for i in range(n+1)] for j in range(4)]
    
    for i in range(1, 4):
        for j in range(1, n+1):
            if arr[i-1]> j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=t[i][j-arr[i-1]] + t[i-1][j]
    return t[3][n]