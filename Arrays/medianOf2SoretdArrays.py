# User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
        # code here
        if len(array1) > len(array2):
            return self.MedianOfArrays(array2, array1)
        n1 = len(array1)
        n2 = len(array2)
        low = 0
        high = n1
        while low <= high:
            cut1 = (low+high)//2
            cut2 = ((n1+n2+1)//2)-cut1
            left1 = -float('inf') if cut1 == 0 else array1[cut1-1]
            left2 = -float('inf') if cut2 == 0 else array2[cut2-1]

            right1 = float('inf') if cut1 == n1 else array1[cut1]
            right2 = float('inf') if cut2 == n2 else array2[cut2]

            if left1 <= right2 and left2 <= right1:
                if (n1+n2) % 2 == 0:
                    val = max(left1, left2)+min(right1, right2)
                    if val % 2 == 0:
                        return val//2
                    else:
                        return val/2

                else:
                    return max(left1, left2)
            elif left1 > right2:
                high = cut1-1
            else:
                low = cut1+1
        return 0.0
