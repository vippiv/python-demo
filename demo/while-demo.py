# while Demo
i = 0
size = 100
while(i < size):
    print("hello python %d" % i)
    i += 1  # i++会报错

print("+" * 100)
print("0-100计算")
k = 0
j = 0
while( j <= 100 ):
    k += j
    j += 1
print(k)

print("+" * 100)
print("偶数求和")
a = 0
r = 0
while(a<=100):
    if a % 2 == 0:
        r += a
    a += 1
print(r)

print("+" * 100)
print("break")
m = 0
while(m<=100):
    print(m)
    if m >= 2:
        break
    m += 1

print("+" * 100)
print("continue")
n = 0
while (n <= 6):
    n += 1
    if n == 2:
        continue
    print(n)
