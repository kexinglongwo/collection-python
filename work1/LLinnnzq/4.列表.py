l = eval(input('输入一个含有整数和字符串的列表'))
cancel = [i for i in l if type(i) == str]
l1 = [i for i in l if (i not in cancel)]
l1.sort()
print(l1)