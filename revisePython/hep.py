from heapq import heappush, heappop

heap=[]

heappush(heap, [0,2])
heappush(heap, [2,1])
heappush(heap, [1,3])

while len(heap):
    print(heappop(heap))