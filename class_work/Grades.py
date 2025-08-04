def Grades(marks):

    if 90<=marks<=100:
       print("A")
    elif 85<=marks<=89:
       print("B+")
    elif 80<=marks<=84:
       print("B")
    elif 70<=marks<=79:
       print("c")
    else:
       print("F")
marks=(int(input()))       
Grades(marks)
