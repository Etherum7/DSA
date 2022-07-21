def bin_add(s:str, t: str)->str:
    if(len(s)> len(t)): 
        t = '0'*(len(s)-len(t))+ t
    else: 
        s = '0'*(len(t)-len(s))+ s
    num1 = list(s)
    num2= list(t)
    # print(num1, num2)
    l = len(s)
    num3 = [0]*len(s)
    carry=0
    
    for i in reversed(range( 0, l)):
        if carry: 
          sum = int(num1[i])+ int(num2[i])+ carry
        else: 
          sum= int(num1[i])+ int(num2[i])

        if sum==2:
            carry=1
            num3[i]=0
        elif sum==3:
            carry=1
            num3[i]=1
        else:
            num3[i] = sum
            carry=0
    if carry:
        num3.insert(0, 1)
    
    return ''.join([str(elm) for elm in num3]) 
a=bin_add('1','0')

print(a)
