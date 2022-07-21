def areRotations(a,b):
    first = a[0]
    j=0
    while j<len(b) and b[j]!=first:
            j+=1
    if(b[j]!=first):
        return False
    for c in a[1:]:
        if(j==len(b)-1):
            j=-1
        if(b[j+1]!=c):
            return False
        j+=1
    return True
def areRotations2(a,b):
    if(len(a)!=len(b)):
        return False
    c=a+a
    if b in c:
        return True
    else:
        return False
print(areRotations2('abcd','cdabc'))
        
