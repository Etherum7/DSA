def validSubstring(s1,s2,s3):
    if(len(s1)!=len(s2)+len(s3)):
        return False
    if sorted(s1)==sorted(s2+s3):
        return True
    else :return False
    
print(validSubstring('1xy2','x2','y1'))