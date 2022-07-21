# Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer.
# Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.

# A slight modification of the problem can be found



def getMinDiff(arr, n, k):
    arr.sort()  # sorting the array
    # it's same as substracting an+k-(ao+k) or an-k-(a0-k)
    ans = arr[n-1]-arr[0]
    small, big = 0, 0

    for i in range(1, n):  # trying to make each tower highest
        small = min(arr[0]+k, arr[i]-k)  # finding minimum tower height
        big = max(arr[i-1]+k, arr[-1]-k)  # finding maximum tower height
        # checking whether we get smaller value as result
        ans = min(ans, big-small)

    return ans


arr = [1, 10, 14, 14, 14, 15]
k = 6
print(getMinDiff(arr, len(arr), k))


arr = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
print(getMinDiff(arr, len(arr), 5))
