def dutch_var_1(A:list):
    zero,one,two=0,0,len(A)
    while one< two:
        if A[one]==0:
            A[zero], A[one] =A[one], A[zero]
            zero+=1
            one+=1
        elif A[one]==1:
            one+=1
        else:
            two-=1
            A[two], A[one] =A[one], A[two]
            
    return
# l=[1,0,2]
# dutch_var_1(l)
# print(l)

def dutch_var_2(A:list):
    one, two, three, four=0,0,0,len(A)
    while three< four:
        if A[three]['key']==1:
            A[one], A[three]= A[three], A[one]
            one+=1
            two+=1
            three+=1
        elif A[three]['key']==2:
            A[two], A[three]= A[three], A[two]
            two+=1
            three+=1
        elif A[three]['key']==3:
            three+=1
        elif A[three]['key']==4:
            four-=1
            A[four], A[three]= A[three], A[four]
# l=[{'key':2},{'key':1},{'key':1},{'key':4},{'key':1},{'key':3}, {'key':2}]
# dutch_var_2(l)
# print(l)

def dutch_var_3(A:list):
    f, u,t=0,0, len(A)
    while u< t:
        if A[u]['key']==False:
            A[f], A[u]= A[u], A[f]
            f+=1
            u+=1
        else:
            t-=1
            A[u],A[t]=A[t],A[u]
# l=[{'key':True, 'key2':1}, {'key':False,'key2':2}, {'key':True, 'key2':3}, {'key':False, 'key2':4}, {'key':True, 'key2':5}, ]
# dutch_var_3(l)
# print(l)

def dutch_var_4(A:list):
    lastTrue=len(A)
    for i in reversed(range(len(A))):
        print(i)
        if(A[i]['key']):
            lastTrue-=1
            A[lastTrue], A[i]=A[i],A[lastTrue]

l1=[{'key':True, 'key2':9},{'key':False,'key2':2},{'key':True, 'key2':1}, {'key':True, 'key2':8}, {'key':True, 'key2':3}, {'key':False, 'key2':4}, {'key':False, 'key2':5} ]
dutch_var_4(l1)
print(l1)
