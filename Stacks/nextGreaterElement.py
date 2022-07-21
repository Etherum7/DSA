def nextGreaterElement(arr, N):
    res=[]
    st=[]
    for i in range(N-1, -1, -1):
        while len(st) and st[-1]<arr[i]:
            st.pop()
        if len(st)==0:
            res.append(-1)
        else:
            res.append(st[-1])
        st.append(arr[i])
    return res[::-1]
print(nextGreaterElement([1,3,2,4],4))
