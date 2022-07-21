def factorial(n):
    if n<=0:
        return 1
    return factorial(n-1)*n
# print(factorial(6))

def printNtoN(n, d):
    if n==1:
        print(1)
        return
    if d==-1:
        print(n)
    printNtoN(n-1, d)
    if d==1:
        print(n)
printNtoN(7, 1)
printNtoN(7, -1)
    
