def longestPalindromic(str):
    n=len(str)
    maxLength=1
    start=0
    for i in range(1,n):
        # even palindrome
        low=i-1
        high=i
        # print(low,high)
        while (low>=0 and high<n and str[low]==str[high]):
            low-=1
            high+=1
        # actual 
        low+=1
        high-=1
        if(str[low]==str[high] and high-low+1 > maxLength):
            # print(low,high)
            maxLength=high-low+1
            start=low
        # odd
        low=i-1
        high=i+1
        while (low>=0 and high<n and str[low]==str[high]):
            low-=1
            high+=1
        # actual 
        low+=1
        high-=1
        if(str[low]==str[high] and high-low+1 > maxLength):
            maxLength=high-low+1
            start=low

    return str[start:start+maxLength]
print(longestPalindromic('aaaabbaa'))
