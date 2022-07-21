class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dmap = {}
        for index, num in enumerate(nums1):
            dmap[num] = index
        st = []
        res = [0]*len(nums1)
        for i in range(len(nums2)-1, -1, -1):
            if nums2[i] in dmap:
                if len(st) == 0:
                    res[dmap[nums2[i]]] = -1
                else:
                    while len(st) and st[-1] < nums2[i]:
                        st.pop()
                    if len(st):
                        res[dmap[nums2[i]]] = st[-1]
                    else:
                        res[dmap[nums2[i]]] = -1
            st.append(nums2[i])
        return res
