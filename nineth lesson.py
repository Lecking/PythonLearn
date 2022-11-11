names=['张赫','张三','小红','老六']
cars=['BMW','honda','BYD','benz']
wants=['李四',"王五","冯七"]
print(names[0],names[1],names[2],names[3])
for i in names:
    print(i)
for i in range(0,4):
    print("早上好",names[i])
for i in range(0,4):
    print(names[i]+'乘坐',cars[i])
for i in wants:
    print(i+'请与我共进晚餐')
print(names[0]+"无法来")
print(wants[0]+"可以来")
names[0]=wants[0]
for i in names:
    print(i)


















































