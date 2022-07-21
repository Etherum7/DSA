def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def sort012(arr: list):
    # dutch national flag
    n = len(arr)
    low = 0
    high = n-1
    mid = 0
    while mid <= high:
        if(arr[mid] == 0):
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif(arr[mid] == 1):
            mid += 1

        elif (arr[mid] == 2):
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr
    


A = [2, 0, 1, 1,  0, 2]
B = sort012(A)
print(B)

# def sort012(arr: list):
#     # 3 list method
#     B = []
#     C = []
#     D = []
#     for index, num in enumerate(arr):
#         if num == 0:
#             B.append(0)

#         if num == 1:
#             C.append(1)

#         if num == 2:
#             D.append(2)

#     arr = B+C+D
#     print(arr)
