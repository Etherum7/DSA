def getSmaller(arr: list, x: int):
    return list(filter(lambda e: e < x, arr))
def getSmaller1(arr: list, x: int): 
    A=[]
    for i in arr:
        if(i<x):
            A.append(i)
    return A
print(getSmaller1([20,30,10,40,78, 65], 32))
