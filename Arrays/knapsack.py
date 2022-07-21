def knapsack(profits, weight, m, n):
    profit_per_weight=[float(profits[i])/weight[i]for i in range(n)]
    x=[0]*n
    total_weight=0
    while total_weight< m:
        ind=profit_per_weight.index(max(profit_per_weight))
        if weight[ind]>m-total_weight:
           x[ind]= float(m-total_weight)/weight[ind]
        else:
            x[ind]=1
        profit_per_weight[ind]=0
        total_weight += weight[ind]
    total_profit =0
    print(x)
    for i in range(n):
        total_profit+=(x[i]*profits[i])
    return total_profit

profits=[10,5,15,7,6,18,3]
weight=[2,3,5,7,1,4,1]
print(knapsack(profits, weight , 15, 7))

