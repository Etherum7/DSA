def evenodd(l:list):
    next_even, next_odd= 0, len(l)-1
    while next_even < next_odd:
        if(l[next_even]%2==0):
            next_even += 1
        else:
            l[next_even], l[next_odd] = l[next_odd], l[next_even]
            next_odd-=1
l=[1,2,3,4,5,6,7,8,9,10,11]
evenodd(l)
print(l)