class FurnitureItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s]%.2f平方米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.type = house_type
        self.area = area

        self.free_area = area
        self.item_list = []

    def __str__(self):

        return "我的房子是[%s]，总面积%.2f，已有家具%s，剩余面积%.2f平方米" % \
               (self.type, self.area, self.item_list, self.free_area)

    def add_item(self, item):

        print("要添加%s" % item)

        if item.area > self.free_area:
            print("对不起，房子里放不下该家具了")
            return

        print("添加成功!")

        self.item_list.append(item.name)

        self.free_area -= item.area


bed = FurnitureItem("床", 10)
desk = FurnitureItem("桌子", 5)
chair = FurnitureItem("椅子", 0.5)

print(bed, desk, chair)

my_house = House("两室一厅", 60)

my_house.add_item(bed)
my_house.add_item(desk)
my_house.add_item(chair)

print(my_house)

