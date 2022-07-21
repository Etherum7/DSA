# User function Template for python3
from collections import deque


class Solution:
    def max_of_subarrays(self, arr, n, k):
        '''
        you can use collections module here.
        :param a: given array
        :param n: size of array
        :param k: value of k
        :return: A list of required values 
        '''
        # code here
        q = deque()
        i = j = 0
        ans = []
        while j < n:
            while len(q) > 0 and arr[j] > q[-1]:
                q.pop()
            q.append(arr[j])

            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                ans.append(q[0])
                if q[0] == arr[i]:
                    q.popleft()
                i += 1
                j += 1
        return ans
