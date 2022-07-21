
def f(ind, N, M, K, ip, dp ):
    if(K==1):
        print(ind)
        if ip[ind]%2==0 and ip[-1]%2:
        #    dp[ind][K]=1
           return 1
        return 0
    if(dp[ind][K]!=-1):
        return dp[ind][K]
    if ip[ind]%2==0:
        for j in range(ind+M, N):
            if ip[j-1]%2:
                dp[ind][K]=0
                dp[ind][K]+=f(j, N, M, K-1, ip,  dp)
        
    else:
        dp[ind][K]=0
    return dp[ind][K]


def solve (N, M, K, S):
    # Write your code here
    ip=[int(ch) for ch in S]
    dp=[[-1 for _ in range(K+1)] for i in range(N)]
    if ip[0]%2 or ip[-1]%2==0 :
        return 0
    # cnt=[0]
    f(0, N, M, K, ip, dp)
    print(dp)
    # return dp[0][K]

    # return cnt[0]
print(solve(6,3,2,'021433'))
# print(solve(5,5,1,'20231'))
# print(solve(4,1,2,'2141'))

# 6
# 3
# 2
# 021433

# 5
# 5
# 1
# 20231

# 4
# 1
# 2
# 2141
    