ori = [[1 for _ in range(5)] for _ in range(10)]

ori[2][2] = 3

print(ori)

new = [ [ ori[i][j] for i in range(10)] for j in range(5) ]

print(new)