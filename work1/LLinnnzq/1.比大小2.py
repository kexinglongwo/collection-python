a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if b > a:
    a, b = b, a
if c > a:
    a, c = c, a
if c > b:
    b, c = c, b
print("%d>=%d>=%d" % (a, b, c))



