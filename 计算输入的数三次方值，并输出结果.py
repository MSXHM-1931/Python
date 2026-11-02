raw = input("请输入一个数字：")

try:
    a = int(raw)
except ValueError:
    a = float(raw)

result = a ** 3
print("{:->20}".format(result) if len(str(result)) >= 20 else "{:-^20}".format(result))
