year1=int(input("enter current year:"))
year2=int(input("enter last year:"))
print("list ofnleapyears:")
for i in range(year1,year2):
    if(i%4==0)and(i%100!=0)or(i%400==0):
        print(i)
