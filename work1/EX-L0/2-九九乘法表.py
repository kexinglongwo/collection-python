#输出九九乘法表
for i in range(1, 10):
    j = 1

    while j<=i:
        if j==i:
         print(j,"*",i,"=",j*i)

        else:
         print(j, "*", i, "=", j * i, " ",end=" ")
        j += 1


