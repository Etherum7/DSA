
import math


def maxMin0(arr):
    final = {}
    final['min'] = min(arr)
    final['max'] = max(arr)
    return final


def maxMin1(arr):
    # linear search
    min = math.inf
    max = -math.inf
    n = len(arr)
    if(n == 1):
        min = arr[0]
        max = arr[0]
    else:
        if(arr[0] > arr[1]):
            min = arr[1]
            max = arr[0]
        else:
            min = arr[0]
            max = arr[1]

        for i in range(2, len(arr)):
            if(arr[i] > max):
                max = arr[i]
            elif(arr[i] < min):
                min = arr[i]

    return {'min': min, 'max': max}


def maxMin2(arr: list, low: int, high: int):
    # tournament method

    if(low == high):
        arr_min = arr[low]
        arr_max = arr[high]
        return (arr_max, arr_min)
    elif(low == high-1):
        if(arr[low] > arr[high]):
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)

    else:
        mid = math.floor((low+high)/2)
        max_elem1, min_elem1 = maxMin2(arr, low, mid)
        max_elem2, min_elem2 = maxMin2(arr, mid, high)

        max_real = max(max_elem1, max_elem2)
        min_real = min(min_elem1, min_elem2)
        return (max_real, min_real)


def maxMin3(arr):
    # compare in pairs
    n = len(arr)
    if n % 2 == 0:
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i = 2
    else:
        mx = mn = arr[0]
        i = 1

    while(i < n-1):
        if(arr[i] < arr[i+1]):
            mx = max(mx, arr[i+1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i+1])
        i+=2
    return (mx, mn)


print(maxMin3([34, 23, - 45, 78, 56]))
