#a shopping mall having 5% for men and 7% for women &individual % for 3* no of items purchage%
n=int(input("No of items:"))
gender=input()
l=[]
l1=[]
for i in range(n):
    input("Item")
    price=int(input("Price of item:"))
    l.append(price)
#print(l)
#sumofitems=sum(l)
#print(sumofitems)
#discount=sumofitems-((3*n*sumofitems)/100)
#print(discount)
for i in l:
    dis=i-((i*n*3)/100)
    print("Discount amount on each item:",dis)
    l1.append(dis)
#print(l1)
soiadis=sum(l1)
print("Bill amount before gender discount:",sum(l1))
if gender.lower()=="male":
    print("Total bill:",soiadis-((soiadis*5)/100))    
elif gender.lower()=="female":
    print("Total bill:",soiadis-((soiadis*7)/100))
else:
    print("Total bill:",soiadis)

