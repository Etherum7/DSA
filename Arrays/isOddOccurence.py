def isOddOccurence(A:list):
    res=0
    for i in A:
        res= res^i
    return res
print(isOddOccurence([10,10,20,30,40,30,40]))