#输入三个整数x,y,z，请尝试用多种方式把这三个数由大到小输出
a,b,c=input().split()
if a<b:
    a, b = b, a
if b<c:
    b, c = c, b
if a < b:
    a, b = b, a
print(a,b,c)