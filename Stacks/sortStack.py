class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def insert(self, st, e):
        if len(st)==0 or st[-1] <= e:
            st.append(e)
            return
        val = st.pop()
        self.insert(st, e)
        st.append(val)
        return

    def sorted(self, st):
        # Code here
        if len(st) == 1:
            return
        val = st.pop()
        self.sorted(st)
        self.insert(st, val)
ob=Solution()
A=[3,2,1]
ob.sorted(A)
print(A)