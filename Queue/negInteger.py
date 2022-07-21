from queue import Queue
def printFirstNegativeInteger( A, N, K):
    # code here
    i=j=0
    
    q=Queue()
    res=[]
    while j<N:
        if A[j]<0:
            q.put(A[j])
            
        if j-i+1<K:
            j+=1
        elif j-i+1==K:
            if not q.empty():
                res.append(q.queue[0])
                if q.queue[0]==A[i]:
                    q.get()
            else:
                res.append(0)
            i+=1
            j+=1
    return res