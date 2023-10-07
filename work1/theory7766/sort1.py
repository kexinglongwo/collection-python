x = int(input('x='))
y = int(input('y='))
z = int(input('z='))

listFirst = [x, y, z]
# 法一：使用列表所带的sorted函数
print("func1:", end="")
list1 = sorted(listFirst, reverse=True)
for i in list1:
    print(i, end=" ")

# 法二：使用算法
print("\nfunc2:", end="")
if (x < y):
    x, y = y, x
    if (y < z):
        y, z = z, y
    elif (x < z):
        x, z = z, x
elif (y < z):
    y, z = z, y
    if (x<y):
        x, y = y, x
print(x, y, z)

# 法三：原地排序
print("func3:", end="")
listFirst.sort(reverse=True)
for i in listFirst:
    print(i, end=" ")