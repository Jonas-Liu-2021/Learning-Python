import random

person = int(input("请输入您要出的拳（1/石头；2/剪刀；3布）： "))

computer = random.randint(1, 3)

print("您出的拳是%d，电脑出的拳是%d" % (person, computer))

if (person - computer == -1
        or person - computer == 2):
    print("您赢了")
elif person - computer == 0:
    print("平局")
else:
    print("您输了")
