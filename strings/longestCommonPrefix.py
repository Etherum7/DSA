# Python 3 Program to find the longest common prefix

# A Function to find the string having the minimum
# length and returns that length
def findMinLength(arr, n):

    min = len(arr[0])

    for i in range(1, n):
        if (len(arr[i]) < min):
            min = len(arr[i])

    return(min)

# A Function that returns the longest common prefix
# from the array of strings


def commonPrefix(arr, n):

    minlen = findMinLength(arr, n)
    result = ""
    for i in range(minlen):

        # Current character (must be same
        # in all strings to be a part of
        # result)
        current = arr[0][i]

        for j in range(1, n):
            if (arr[j][i] != current):
                return result

        # Append to result
        result = result+current

    return (result)


# Driver program to test above function
if __name__ == "__main__":

    arr = ["geeksforgeeks", "geeks",
           "geek", "geezer"]
    n = len(arr)

    ans = commonPrefix(arr, n)

    if (len(ans)):
        print("The longest common prefix is ", ans)
    else:
        print("There is no common prefix")
