from datetime import date,datetime
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.weekday())
print(today.isoweekday())

now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)  

print(now.hour)
print(now.minute)
print(now.second)