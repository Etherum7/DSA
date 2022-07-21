from typing import List
from queue import Queue


class Solution:
    def isStackPermutation(self, N: int, A: List[int], B: List[int]) -> int:
        # code here
        st = []
        ip = Queue()
        op = Queue()
        for i in range(N):
            ip.put(A[i])
            op.put(B[i])

        while not ip.empty():
            ele = ip.queue[0]
            ip.get()
            if ele == op.queue[0]:
                op.get()
                while len(st):
                    if st[-1] == op.queue[0]:
                        st.pop()
                        op.get()
                    else:
                        break
            else:
                st.append(ele)

        return int(ip.empty() and len(st) == 0)

# stack<int> st;
#        int j = 0;
#        for(int i = 0; i < N; i++){
#            st.push(A[i]);

#            while(!st.empty() && st.top() == B[j]){
#                st.pop();
#                j++;
#            }
#        }

#        if(st.empty()){
#            return 1;
#        }
#        return 0;
