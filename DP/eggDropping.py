# User function Template for python3

class Solution:

    # Function to find minimum number of attempts needed in
    # order to find the critical floor.
    def __init__(self):
        self.t = {}

    def convert(self, n, k):
        return str(n)+' ' + str(k)

    def eggDrop(self, e, f):
        # code here
        if e == 1 or f == 0 or f == 1:
            return f
        key = self.convert(e, f)
        if key in self.t:
            return self.t[key]
        mn = float('inf')
        for k in range(1, f+1):
            lowkey = self.convert(e-1, k-1)
            highkey = self.convert(e, f-k)
            if lowkey in self.t:
                low = self.t[lowkey]
            else:
                low = self.eggDrop(e-1, k-1)
                self.t[lowkey] = low
            if highkey in self.t:
                high = self.t[highkey]
            else:
                high = self.eggDrop(e, f-k)
                self.t[highkey] = high
            temp = 1 + max(low, high)
            mn = min(mn, temp)
        self.t[key] = mn
        return mn
# real
def binomialCoeff(x, n, k):
 
    sum = 0;
    term = 1;
    i = 1;
    while(i <= n and sum < k):
        term *= x - i + 1;
        term /= i;
        sum += term;
        i += 1;
    return sum;
 
# Do binary search to find minimum
# number of trials in worst case.
def minTrials(n, k):
 
    # Initialize low and high as
    # 1st and last floors
    low = 1;
    high = k;
 
    # Do binary search, for every
    # mid, find sum of binomial
    # coefficients and check if
    # the sum is greater than k or not.
    while (low < high):
 
        mid = int((low + high) / 2);
        if (binomialCoeff(mid, n, k) < k):
            low = mid + 1;
        else:
            high = mid;
 
    return int(low);