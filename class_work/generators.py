def feed(l):
    for i in l:
        yield i

l=["file1","file2","file3","file4"]

load=feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))
#example
def simple_generator():
    print("start")
    yield 1
    yield 2
    yield 3
    print("End")
gen=simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
#example
def count_up_to(n):
    count=1
    while count <=n:
        yield count
        count+=1
counter=count_up_to(5)
print(next(counter))  
print(next(counter))
print(next(counter))        
print(next(counter))        
print(next(counter))        