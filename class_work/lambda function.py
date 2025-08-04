l=["vishwas","goutham","srikanth"]
squ=list(map(lambda i:i.title(),l))
print(squ)

print('=========')

l=["vishwas","goutham","srikanth"]
squ=list(map(lambda i:i.upper(),l))
print(squ)

print('=========')

l="vishwas"
vol="aeiou"
squ=list(map(lambda i:'*' if i in vol else i,l))
print(squ) 

#filter function
l=[1,2,3,0,0,8,9,8,0,0,9,1,3,4,0,9,0,0]
squ=list(filter(lambda i:i!=0,l))
print(squ)

#reduce function
from functools import reduce
numbers=[1,2,3,4,5]
num_all=reduce(lambda x,y:x+y,numbers)
print(num_all)