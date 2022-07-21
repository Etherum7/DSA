from queue import Queue
def interLeaveQueue(q):
    st=[]
    size=q.qsize()
    if size%2:
        return False
    halfsize=size//2
    for i in range(halfsize):
        st.append(q.get())
    while len(st):
        q.put(st.pop())
    for i in range(halfsize):
        q.put(q.get())
    for i in range(halfsize):
        st.append(q.get())
    for i in range(halfsize):
        q.put(st.pop())
        q.put(q.get())
    
if __name__ == '__main__':
    q = Queue()
    q.put(11)
    q.put(12)
    q.put(13)
    q.put(14)
    q.put(15)
    q.put(16)
    q.put(17)
    q.put(18)
    q.put(19)
    q.put(20)
    interLeaveQueue(q)
    length = q.qsize()
    for i in range(length):
        print(q.queue[0], end = " ")
        q.get()