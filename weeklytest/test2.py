#1 question
salary=float(input())
if salary <= 25000 :
    print("No tax")
elif salary >25000 and salary <=500000:
    print(salary*0.05) 
elif salary >500000 and salary <=1000000:
     print(salary*0.2)
elif salary >1000000:
   print(salary*0.3) 

#2 question
n=int(input())
total=0
for _ in range(n):
    age=int(input())
    if age>=5 and age<=18:
        total+=100
    elif age>19 and age<=60:
        total+=150
    elif age>60:
        total+=120
print(total)
#3 question
units=int(input())
bill=0
if units <=100:
    bill+=units*1.5
elif units>100 and units<=200:
    bill+150+(units-100)*2.5
elif units>200 and units<=500:
    bill+=400+(units-200)*4
else:  
    bill+=1600+(units-500)*6
print(bill) 
#4 question
hrs=int(input())
fee=0
if hrs<=2:
    fee=30
    print(fee)
elif hrs>2 and hrs<24:
    fee=30+(hrs-2)*10
elif hrs>=24:
    print(200)
#5 question
name=input()
qua=int(input())
if qua==0:
    print("out of stock")
elif qua>>0 and qua<11:
    print("low stock")
elif qua>10 and qua<51:
    print("In stock")
elif qua>50:
    print("over stock")

#6 question
n=int(input())
for row in range(n):
    for col in range(n):
        if(row+col)%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()
#7 question
ch=int(input())
ppl=int(input())
if ch==1:
    print(ppl*500)
elif ch==2:
    print(ppl*1300)
elif ch==3:
    print(ppl*5000)
#8 question
total=float(input())
if total<1000:
    print(total)
elif total>999 and total<5000:
    print(total-total*0.05)
elif total>4999 and total<10000:
    print(total-total*0.1)
elif total>10000:
    print(total-total*0.15)
#9 question
pin=1234
for _ in range(3):
    epin=int(input())
    if epin==pin:
        print("Access Granted")
        break
else:
    print("ATM Blocked. Try Again Later")
#10 question 
total_seats=int(input())
booked_seats=list(map(int,input().split()))
print(f'Total seats:{total_seats}')
print(f'Booked:{len(booked_seats)}')
print(f'Available:{total_seats-len(booked_seats)}')