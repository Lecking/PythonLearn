i=0
a="2722702142"
c="2722702142"
for i in range(3):
    aa = str(input("输入账号:"))
    cc= str(input("输入密码:"))
    if a==aa and c==cc :
        print("登录成功！")
        break
    else:
        print("账号或密码错误")
        print("您还有{}次机会".format(2-i))
        i=i+1
        if i >= 3:
            print(" 已错误3次！")
            print("错误，账号被锁定!   错误，账号被锁定!    错误，账号被锁定!    错误，账号被锁定!    错误，账号被锁定!    错误，账号被锁定!    错误，账号被锁定!    错误，账号被锁定!    错误，账号被锁定!")











