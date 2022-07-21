def unionMerge(arr1, arr2):
    n=len(arr1)
    m=len(arr2)
    c=[]
    i,j=0,0
    prev=None
    while i< n and j<m:
        if(arr1[i]<arr2[j]):
            if prev != arr1[i]:
              c.append(arr1[i])
              prev=arr1[i]
            i+=1
        elif(arr1[i]>arr2[j]):
            if prev != arr2[j]:
              c.append(arr2[j])
              prev=arr2[j]
            
            j+=1
        else:
            if prev != arr1[i]:
               c.append(arr1[i])
               prev=arr1[i]
            i+=1
            j+=1
    while i<n:
        if arr1[i]!=prev:
          c.append(arr1[i])
          prev=arr1[i]
        i+=1
    while j<m:
        if arr2[j]!=prev:
          c.append(arr2[j])
          prev=arr2[j]
        j+=1
    return c

def intersectionMerge(arr1, arr2):
    n=len(arr1)
    m=len(arr2)
    i,j=0,0
    c=[]
    while i<n and j<m:
        if(arr1[i]==arr2[j]):
            c.append(arr1[i])
            while i<n and c[-1] == arr1[i]:
                i+=1
            while j <m and c[-1]==arr2[j]:
                j+=1
        elif(arr1[i]<arr2[j]):
            i+=1
        else:
            j+=1
    return c




