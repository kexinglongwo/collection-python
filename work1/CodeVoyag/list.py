old_list = ["a", "b", "c", 1, 2, 3,]
out = [i for i in old_list if type(i) == int]
print(sorted(out))