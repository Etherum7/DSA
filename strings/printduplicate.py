def printDuplicate(s):
    res={}
    
    for i in range(len(s)):
        if s[i] in res:
            res[s[i]] +=1
        else:
            res[s[i]] =1
    for key, value in res.items():
        if(value>1):
          print(f'{key} repeated {value} times ')
printDuplicate('aa')

