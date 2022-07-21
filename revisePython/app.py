# lists
# mylist=['apple','cherry']
# print(mylist[-2])

# mylist2=list()



# for fruit in mylist:
#     pass
#     print(fruit)

# mylist2.append('banana' )
# mylist2.extend(['mango','jamuna'])
# l=[-1,4,2,3]
# m=n=[0,1,2]
# print(dir(l))
# print(l.sort()==l.sort())
# m.sort()
# print(m==n)

# mylist2.remove('banana')
# print(mylist2)

# # slicing
# mylist=list(range(0,10))
# a=mylist[0::2]
# print(a) 

# Tuples

# mytuple=('aloo','sona','rahul', 200000, 250000)
# print(mytuple[3])

# friend1, friend2, friend3, *salary=mytuple
# # print(friend1, friend2, friend3, salary)
# mylist=list(mytuple)
# import sys
# print(sys.getsizeof(mytuple))
# print(sys.getsizeof(mylist))

# import timeit
# print(timeit.timeit(stmt="('aloo','sona','rahul', 200000, 250000)", number=1000000))
# print(timeit.timeit(stmt="['aloo','sona','rahul', 200000, 250000]", number=1000000))

# dictionary

mydict={'name':"Harsh", 'age':20}

# mydict2=dict(name="Harsh", age=21)

# print(mydict['name'])

# mydict['email']='xyz@xyz.gmail.com'

# if 'name' in mydict:
#     print('yes')
# try:
#     print(mydict['lastname'])
# except KeyError:
#     print('Keyerror')
# except Exception as e:
#     print('No key of '+ str(e.__class__))
# t1={i:i**2 for i in range(1, 10)}
# print(t1)
# t2={}
# t2[(1,2)]=3
# t2[(4,5)]=6

# print(t2)

# ms='   Hello  '
# ms=ms.strip()
# ms=ms.lower()
# ms=ms.upper( )
# print(ms)
from timeit import default_timer as timer
from collections import Counter, OrderedDict, defaultdict, namedtuple, deque
# start=timer()
s='abrazzcadabrazz'
my_counter=Counter(s)
print(my_counter)

# print(''.join(sorted(list(my_counter.elements()))))
# stop=timer()
# print(stop-start)

# d=OrderedDict()
# i=1
# d=d.fromkeys(['a','b','c','d','e','f','g','h'],value=[1,2,3,4,5,6,7,8])
# print(d)
# print(d['a'])

# c= defaultdict(str)
# print(c[1])

# Car=namedtuple('Car','color, brand, price')

# t=Car('red', 'honda', '11 lakh')
# print(t.price)

# d=deque()
# d.extend([1,2,3])
# d.extendleft([-1,-2,-3])
# d.pop()
# d.popleft()

# d.rotate(3)
# d.clear()
# print(d)

import logging





