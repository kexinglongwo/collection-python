import random
global dizhu
def wrichangestr(a):
    b=""
    for i in a:
        b=b+i+"  "
    return b
def FAPAI():

    
    b=["2","3","4","5","6","7","8","9","10","J","K","Q","A"]
    c=["梅花","方块","红桃","黑桃"]
    a=[]
    player=[1,2,3]
    player_=[1,2,3]
    dizhu=0
    for i in c:
        a.extend(i+j for j in b)
    dizhu=0

    flag=0
    while True:
        random.shuffle(a)
        for i in range(1,4):
            print("是否选择叫地主,请回答是或不是")
            choice=input()
            if choice=="是":
                dizhu=i
                flag=1
            if flag==1:
                break
        break
    player.pop(dizhu-1)


    for i in player:
        print("是否抢地主")
        choice1=input("回答是或不是\n")
        if choice1=="是":
            dizhu=i
    print("地主是",dizhu)
    player_.pop(dizhu-1)
    for i in player_:
        print("农民是",i)

    p="player"
    pingming = [f"player{str(i)}" for i in player_]
    for i in range(len(pingming)):
        with open(f"{pingming[i]}.txt", "w+", encoding="utf-8") as t:
            t.write(wrichangestr(a[i*17:i*17+17]))
    with open(f"player{str(dizhu)}.txt", "w+", encoding="utf-8") as p:
        p.write(wrichangestr(a[34::]))

FAPAI()