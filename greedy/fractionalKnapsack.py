
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        res=0
        Items.sort(key = lambda x: x.value/x.weight, reverse=True)
        i=0
        while i<n and W>0:
                if W<Items[i].weight:
                    res+=(Items[i].value/Items[i].weight)*W
                    break
                else:
                    res+=Items[i].value
                    W-=Items[i].weight
                i+=1
        return res