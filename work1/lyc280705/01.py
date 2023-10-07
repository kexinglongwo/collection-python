#方法1
X=int(input())
Y=int(input())
Z=int(input())
if X<Y:
    if Y<Z:
        print(Z,Y,X)
    elif X>Z:
        print(Y,X,Z)
    else:
        print(Y,Z,X)
elif Y<Z:
    if X>Z:
        print(X,Z,Y)
    else:
        print(Z,X,Y)
else:
    print(X,Y,Z)

numbers = [int(input()) for _ in range(3)]
numbers.sort(reverse=True)
for j in numbers:
    print(j,end=" ")