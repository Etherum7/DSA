

def f(start, end, n,price, dp):
    age=n-(end-start)
    if(start == end):
        return age*price[start]
    if(dp[start][end]!=-1):
        return dp[start][end]

    pickStart = price[start]*age+f(start+1, end,n, price, dp)
    pickEnd = price[end]*age+f(start, end-1,n, price, dp)
    dp[start][end]=max(pickStart, pickEnd)
    return dp[start][end]


def maxProfit(price, size):
    dp=[[0]*(size) for i in range(size)]
    

    return f(0, size-1, size,price, dp)

    


price = [2, 4, 6, 2, 5]

size = 5

ans = maxProfit(price, size)

print(ans)
