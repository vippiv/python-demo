# 逻辑运算符，与and，或or，非not
i = 10
j = 20
print("与判断")
if i < 30 and j < 30:
    print("都成立")
else:
    print("有条件不成立")

print("+" * 100)
print("或判断")
if i < 15 or j < 15:
    print("都成立")
else:
    print("有条件不成立")

print("+" * 100)
print("非判断")
is_employee = True
if not(is_employee):
    print("不是本公司员工，禁止入内")
else:
    print("是本公司员工")
