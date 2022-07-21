def average(l: list):
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return sum/len(l)

def average1(l:list):
    return sum(l)/len(l)
print(average1([1,2,3,4,7,6]))


