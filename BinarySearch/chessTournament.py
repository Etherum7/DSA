def isValid(positions, n, c, mid):
    nPlayer = 1
    pos = 0
    for i in range(1, n):
        if positions[i] >= positions[pos]+mid:
            nPlayer += 1
            pos = i
    if nPlayer < c:
        return False
    return True


def chessTournament(positions, n, c):
    positions.sort()
    start = 0
    end = positions[-1]-positions[0]
    res = -1
    while start <= end:
        mid = (start+end)//2
        if isValid(positions, n, c, mid):
            res = mid
            start = mid+1
        else:
            end = mid-1
    return res


print(chessTournament([5, 4, 2, 1], 4, 2))
print(chessTournament([6, 7, 9, 13, 15, 11], 6, 4))
print(chessTournament([
    15, 13, 11, 9, 7, 6], 6, 4))
# 6 4
# 6 7 9 13 15 11
