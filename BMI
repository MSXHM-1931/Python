`python
weight = float(input("请输入体重（kg）："))
height = float(input("请输入身高（m）："))

bmi = weight / (height ** 2)
print("您的BMI值为：{:.2f}".format(bmi))

# 国际BMI分类
if bmi < 18.5:
    international = "偏瘦"
elif bmi < 25:
    international = "正常"
elif bmi < 30:
    international = "超重"
else:
    international = "肥胖"

# 国内BMI分类
if bmi < 18.5:
    domestic = "偏瘦"
elif bmi < 24:
    domestic = "正常"
elif bmi < 28:
    domestic = "超重"
else:
    domestic = "肥胖"

print("国际分类：{}".format(international))
print("国内分类：{}".format(domestic))
`
