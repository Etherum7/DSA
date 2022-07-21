def ispalindrome(s:str)->bool:
    return all(s[i] ==s[~i]for i in range(len(s)//2))
    # reduce func seg initializer