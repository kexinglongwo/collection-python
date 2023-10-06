import random
list = [[1 for _ in range(5)] for _ in range(10)]
for item in list:
    print(item)
lst=[[list[i][j] for i in range(len(list))]for j in range(len(list[0]))]
for item_ in lst:
    print(item_)