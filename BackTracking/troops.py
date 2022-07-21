from heapq import heappush, heappop


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        heap = []

        N = len(A)
        mn = min(A)
        day = mn
        for i in range(N):
            if A[i] != mn:
                heappush(heap, -1*A[i])

        x = 2
        troops = 2
        tDestroy = 1

        while tDestroy != N:
            temp = []
            while len(heap):
                t = heappop(heap)
                if -t <= troops:
                    troops = 0

                    tDestroy += 1
                    x += 1
                    break
                else:
                    temp.append(t)
            for i in range(len(temp)):
                heappush(heap, temp[i])

            troops += x
            day += 1
        return day-1
ob=Solution()
print(ob.solve([28554106, 94463815, 23370472]))
