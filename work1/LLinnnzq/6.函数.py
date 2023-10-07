def CountNum(l1):
    result1 = []
    return {i: l1.count(i) for i in l1 if i not in result1}


yourlist = eval(input('输入一个只有数字的列表'))
print(CountNum(yourlist))
