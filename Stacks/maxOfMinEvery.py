# The appraoch is quite straight forward. Find the previous and next smaller elements to get the window of size the element fits in and fix this value to its correct place, you can also see the hints video

# User function Template for python3

class Solution:

    # Function to find maximum of minimums of every window size.
    def maxOfMin(self, arr, n):
        # code here
        st = []

        left = [-1]*(n+1)
        right = [n]*(n+1)
        # nsr
        # nsl
        for i in range(n-1, -1, -1):
            while len(st) and arr[st[-1]] >= arr[i]:
                st.pop()
            if len(st):
                right[i] = st[-1]
            else:
                right[i] = n
            st.append(i)

        st = []
        for i in range(n):
            while len(st) and arr[st[-1]] >= arr[i]:
                st.pop()
            if len(st):
                left[i] = st[-1]
            else:
                left[i] = -1
            st.append(i)
        # print(right, left)
        ans = [0]*(n+1)
        for i in range(n):
            LenInterval = right[i]-left[i]-1
            ans[LenInterval] = max(ans[LenInterval], arr[i])
        for i in range(n-1, 0, -1):
            ans[i] = max(ans[i], ans[i+1])
        return ans[1:]
