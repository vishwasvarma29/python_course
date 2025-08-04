def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def exp(a,b):
    return a**b
stmt=input()
a=None
b=None
op=None
for i in stmt:
    if not i.isdigit():
        a,b=stmt.split(i)
        op=i
a,b=int(a),int(b)
print(a,b,op)
if op=="+":
    print(sum(a,b))
if op=="-":
    print(sub(a,b))
if op=="*":
    print(mul(a,b))
if op=="/":
    print(div(a,b))
if op=="%":
    print(mod(a,b))
if op=="**":
    print(exp(a,b))              
#addition
def add(a,b):
    return a+b
print(add(10,33))
#subtraction
def sub(a,b):
    return a-b
print(sub(10,33))
#max
def maximum(a,b):
    return max(a,b)
print(maximum(10,33))
#minimum
def minimum(a,b,c,d):
    return min(a,b,c,d)
print(minimum(10,33,44,1))
#sorted
def sort(l):
    return sorted(l)
print(sort([2,3,4,5,0]))