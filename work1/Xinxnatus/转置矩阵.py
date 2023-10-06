def produce():
    return [[1 for _ in range(10)] for _ in range(5)]


def transpose(matrix):
    return [
        [matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]


a = produce()
for i in a:
    print(*i, sep=' ')
print('')

b = transpose(a)
for j in b:
    print(*j,sep=' ')