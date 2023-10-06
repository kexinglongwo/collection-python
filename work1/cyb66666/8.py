#尝试用所学的知识写一个斗地主随机发牌程序，
# 将每个人的发牌以及多的三张牌的结果分别输出到player1.txt，player2.txt，player3.txt，others.txt四个文件中，可以不要求牌的花色
import random
from typing import List

player1=[]
player2=[]
player3=[]
card = []
for i in range(1, 14):
    for _ in range(4):
        if i==1:
            card.append('A')
        elif i==11:
            card.append('J')
        elif i==12:
            card.append('Q')
        elif i==13:
            card.append('K')
        else:
            card.append(i)
card.extend(('JOKER', 'joker'))
for _ in range(10):
    random.shuffle(card)
for i in range(0, 51, 3):
    player1.append(card[i])
    player2.append(card[i+1])
    player3.append(card[i+2])
others = [card[51], card[52], card[53]]
p1=open("player1.txt","w")
p1.writelines(str(player1))
p2=open("player2.txt","w")
p2.writelines(str(player2))
p3=open("player3.txt","w")
p3.writelines(str(player3))
o=open("others.txt","w")
o.writelines(str(others))


