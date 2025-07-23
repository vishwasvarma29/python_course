def update(n):
    print("Before- inside the function",n)
    n=n+10
    print("Before- inside the function",n)
n=10
update(n)
print("outside of the function",n)

print('=======')
def update(n):
    print("Before- inside the function",n)
    n[6]=36
    print("Before- inside the function",n)
n={1:1,2:4,3:7}
update(n)
print("outside of the function",n)
print('=======')
def update(n):
    print("Before- inside the function",n)
    n=False
    print("Before- inside the function",n)
n=True
update(n)
print("outside of the function",n)
print('=======')
def update(n):
    print("Before- inside the function",n)
    n=n.copy()
    n=n.append(20)
    print("Before- inside the function",n)
n=[1,2,3]
update(n)
print("outside of the function",n) 

