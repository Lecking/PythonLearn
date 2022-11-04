import random

n = random.randint(1,15)
for i in range(1,6):
    if i == 4:
        print("                                     !!!还剩一次机会!!!")
    b = int(input("输入你猜的数字"))
    if b < n:
        print("小了")
    elif b > n:
        print("大了")
    else:
        print("正好")

print("结束")
