from datetime import date
d1 = int(input("input start day: "))
m1 = int(input("input start month: "))
y1 = int(input("input start year: "))
startdate = date(y1, m1, d1)
d2 = int(input("input end day: "))
m2 = int(input("input end month: "))
y2 = int(input("input end year: "))
enddate = date(y2, m2, d2)
days = enddate - startdate
print(days.days)
