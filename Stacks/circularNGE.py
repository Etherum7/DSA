class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        for i in range(n-1, -1, -1):
            st.append(nums[i])
        res = []
        for i in range(n-1, -1, -1):
            if len(st) == 0:
                res.append(-1)
            else:
                while len(st) and st[-1] <= nums[i]:
                    st.pop()
                if len(st):
                    res.append(st[-1])
                else:
                    res.append(-1)
            st.append(nums[i])
        return res[::-1]
