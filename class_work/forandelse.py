for i in range(1,11):
    print(i)
else:
    print("End the numbers")

#while

bullets=10
while bullets>0:
    if bullets==6:
       print("Dead")
       break
    print(f"{bullets} are left-you can shoot()")
    bullets-=1
else:
    print("Game over")
