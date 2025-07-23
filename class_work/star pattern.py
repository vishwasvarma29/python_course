n=5
for rows in range(5):
        for columns in range(rows+1):
           print("*",end=" ")
        print()

print('======')
n=5
for rows in  range(5):
      for columns in range(n):
            print("*",end=" ")
      print()
      
print('======')
n=5
for i in range(n):
      for j in range(n):
            print(i,end=" ")  

      print()
print('=====')
n=5
for i in range(n):
      for j in range(n-i):
            print("*",end=" ")
      print()
print('=====')
n=5
for i in range(n):
      for j in range(n-i-1):
            print(" ",end=" ")
      for k in range(i+1):
            print("*",end=" ")
      print()
print('=====')
n=5
for i in range(n):
      for j in range(i+1):
            print(" ",end=" ")
      for k in range(n-i):
            print("*",end=" ")
      print()