def sort(arr):
    if len(arr) ==1:
        return
    temp=arr.pop()
    sort(arr)
    insert(arr, temp)
def insert(arr, temp):
    if len(arr)==0 or arr[-1]<=temp:
        arr.append(temp)
        return
    val= arr.pop()
    insert(arr, temp)
    arr.append(val)
    return
arr=[2,3,7,6,4,5,9]
sort(arr)
print(arr)

