# User function Template for python3
class Solution:

    # Function to find if there exists a triplet in the
    # array A[] which sums up to X.
    def find3Numbers(self, A, n, X):
        # Your Code Here
        if n <= 2:
            return False
        A.sort()

        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                cur = A[i]+A[j]+A[k]
                if cur == X:

                    return True
                elif cur > X:
                    k -= 1
                else:
                    j += 1
        return False
