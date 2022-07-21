class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        st = []
        res = []
        for i in range(len(A)):
            if len(st) == 0:
                res.append(-1)
            else:
                while len(st) and st[-1] >= A[i]:
                    st.pop()
                if len(st):
                    res.append(st[-1])
                else:
                    res.append(-1)
            st.append(A[i])
        return res
