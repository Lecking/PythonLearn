fen=float(input("请输入分数："))
if fen >= 60:
    if fen>=80:
        print("优秀")
    else:
        print ("成绩一般")
else:
    if 30<fen<60:
        print("还有救")
    else:
        print("学渣啊")

