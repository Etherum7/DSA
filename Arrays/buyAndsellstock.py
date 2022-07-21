def buyAndSellStock(prices):
    min_price_so_far=float('inf')
    max_profit=0
    for i in range(len(prices)):
        min_price_so_far=min(prices[i], min_price_so_far)
        max_profit = max(prices[i]-min_price_so_far, max_profit)
    return max_profit
print(buyAndSellStock([7,9,99, 6,4]))

import math
class Solution:
    def maxCrossSubArraySum(self, arr , low, mid, high):
        left_sum=-math.inf
        sum=0
        max_left=mid
        for i in range(mid, low-1, -1):
            sum+=arr[i]
            if sum> left_sum:
                left_sum=sum
                max_left=i
        right_sum=-math.inf
        sum=0
        max_right=mid+1
        for i in range(mid+1, high+1):
            sum+=arr[i]
            if sum> right_sum:
                right_sum=sum
                max_right=i
        return (max_left, max_right, left_sum+right_sum )
        

    def maxSubArraySum(self, arr, low, high):
        if low==high:
            return (low, high, arr[low])
        mid=(low+high)//2
        (leftLow, leftHigh, leftSum)=self.maxSubArraySum(arr, low, mid)
        (rightLow, rightHigh, rightSum)=self.maxSubArraySum(arr, mid+1, high)
        (crossLow, crossHigh, crossSum)=self.maxCrossSubArraySum(arr, low, mid, high)
        if leftSum>=rightSum and leftSum>=crossSum:
            return (leftLow, leftHigh, leftSum)
        elif rightSum>=leftSum and rightSum>=crossSum:
            return (rightLow, rightHigh, rightSum)
        elif crossSum>=rightSum and crossSum>=leftSum:
            return (crossLow, crossHigh, crossSum)
            
    def maxProfit(self, prices: List[int]) -> int:
        
        differnces=[0]+[prices[i]-prices[i-1] for i in range(1,len(prices))]
        (left, right, max_profit)= self.maxSubArraySum(differnces,0, len(differnces)-1 )
        return max_profit
        
        
                
                
        
        