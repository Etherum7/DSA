# User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n > m:
            return self.kthElement(arr2, arr1, m, n, k)
        low = max(0, k-m)
        high = min(n, k)
        while low <= high:
            cut1 = (low+high)//2
            cut2 = k-cut1
            l1 = -float('inf') if cut1 == 0 else arr1[cut1-1]
            l2 = -float('inf') if cut2 == 0 else arr2[cut2-1]
            r1 = float('inf') if cut1 == n else arr1[cut1]
            r2 = float('inf') if cut2 == m else arr2[cut2]

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = cut1-1
            else:
                low = cut1+1
