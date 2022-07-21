class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        res=[]
        st=[]
        for i in range(n):
            while len(st) and st[-1][0]<=a[i]:
                # equal because we are ignoring 
                st.pop()
                
            if len(st)==0:
                res.append(-1)
            else:
                res.append(st[-1][1])
            st.append((a[i], i))
        for i in range(n):
            res[i]= i-res[i]
        return res
# class Solution:

#     # Function to calculate the span of stockâ€™s price for all n days.
#     def calculateSpan(self, a, n):
#         # code here
#         #  ngl
#         st = []
#         res = []
#         for i in range(n):
#             cnt = 1
#             while len(st) and st[-1][1] <= a[i]:
#                 cnt += st[-1][0]
#                 st.pop()
#             res.append(cnt)
#             st.append((cnt, a[i]))
#         return res

