def isValid(stalls, k, n, mid):
    noOfCows = 1
    lastPos = stalls[0]
    for i in range(1, n):
        if stalls[i] >= lastPos+mid:
            noOfCows += 1
            lastPos = stalls[i]

    return noOfCows >= k
def aggressiveCows(stalls, k):
    # Write your code here.
    stalls.sort()
    n = len(stalls)
    start = 0
    end = stalls[-1]
    res = 0
    while start <= end:
        mid = (start+end)//2
        if isValid(stalls, k, n, mid):
            res = mid
            start = mid+1
        else:
            end = mid-1
    return res
