class Solution:
    def leftSmaller(self, n, a):
        # code here
        res = []
        st = []
        for i in range(n):
            while len(st) and st[-1] >= a[i]:
                st.pop()
            if len(st) == 0:
                res.append(-1)
            else:
                res.append(st[-1])
            st.append(a[i])
        return res
