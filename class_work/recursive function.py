def sumofnum(n):
    if n==0:
        return 0
    return n+sumofnum(n-1)
n=6
print(sumofnum(n))
print('=====')
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=int(input ("Enter the value: "))
print(factorial(n))
print('=====')
def shoot(n):
    if n==1:
        return 1
    print("Before recursion:",n)
    shoot(n-1)
    print("After recursion:",n)
n=int(input ("Enter the value: "))
print(shoot(n))
print('=====')
n=(input("Enter thr number(): "))
sum=0
for i in n:
    sum+=int(i)
    print(sum)
    print('=======')
n=int(input("Enter a number: "))
a=0
b=1
if n==1:
    print(a)
elif n>=2:
     print(a)
     print(b)
for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c