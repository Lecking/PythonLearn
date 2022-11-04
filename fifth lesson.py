year=int(input("输入年份:"))
if year%400==0 and year%100!=0 or year%4==0:
    print("是闰年")
else:
    print("是平年")








