class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda val: val[0])
        n = len(intervals)
        st = []
        st.append(intervals[0])
        for i in range(1, n):
            if intervals[i][0] <= st[-1][1]:
                t = st.pop()
                st.append([t[0], max(intervals[i][1], t[1])])
            else:
                st.append(intervals[i])
        return st
