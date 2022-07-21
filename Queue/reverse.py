import sys
sys.setrecursionlimit(10**7)
def rev(q):
    # add code here
    
    if len(q.queue)==1:
        return q
    val=q.get()
    rev(q)
    q.put(val)
    return q