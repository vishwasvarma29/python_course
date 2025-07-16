g_s={
    1:{'product':'rice','price':60},
    2:{'product':'wheat Flour','price':45},
    3:{'product':'sugar','price':40},
    4:{'product':'Milk','price':25},
    5:{'product':'Eggs (12 pcs)','price':70},
    6:{'product':'cooking oil','price':130},
    7:{'product':'Tea Powder','price':90},
    8:{'product':'salt','price':20},
    9:{'product':'Bread','price':30},
    10:{'product':'soap','price':25},
}
print("Enter the product indexes you want to buy(you can repeat indexes)")
print("Here are the availble products:")
print("Index \tproduct \t\tprice (rs.)")
for i in g_s.keys():
    print(f"{i} \t{g_s[i]['product'].ljust(7)} \t{g_s[i]['price']}")
items=list(map(int,input("Enter inex(e.g 1 2 3 4):").split())) 
print("Index \tproduct \tcount \tprice (rs.) \tTotal")  
t=0
ids=set() 
c=0
for j in items:
    if j not in ids:
        c=items.count(j)
        t+=g_s[j]['price']*c
        print(f"{j} \t{g_s[j]['product'].ljust(7)} \t{c}\t\t{g_s[i]['price']} \t\t{t}")
        ids.add(j)
print("Total Bill:",t)