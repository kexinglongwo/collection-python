old_list = ["Alice", "Bob", "Da", 114514, 1919810, 233333, 6666]
out = [i for i in old_list if type(i) == int]
print(sorted(out))
