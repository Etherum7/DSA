def merge(arr1, arr2, n, m): 
        # code here
        j=0
        for i in range(n):
            if(arr1[i]>arr2[j]):
                arr1[i],arr2[j]=arr2[j],arr1[i]
                arr2.sort()
A=[1]
B=[]
merge(A,B, len(A), len(B))
print(A,B)