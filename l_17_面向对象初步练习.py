class WarPlane:

    def __init__(self, long):
        self.long = long

        print("飞机的长是%d米" % plane_long)

    def __del__(self):

        print("此飞机已销毁")

    def __str__(self):
        return "飞机上天了"


Jack = WarPlane(20)
print("结束了")

print(Jack)

