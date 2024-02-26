year=int(input())
if year%400==0:
    print("it is leap year")
elif year%4==0 and year%100!=0:
    print("it is leap year")
else:
    print("it is not leap year")
#print("leap year" if (year%4==0 and year%100!=0) or year%400==0 else "not leap year")
