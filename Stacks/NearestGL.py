def ngl(arr, n):
    res=[]
    st=[]
    for i in range(n):
        while len(st) and st[-1]<arr[i]:
            st.pop()
        if len(st)==0:
            res.append(-1)
        else:
            res.append(st[-1])
        st.append(arr[i])
    return res
print(ngl([1,3,2,4],4))