name_list = [
    {"name": "Tom"},
    {"name": "John"}
]

find_name = input("请输入你要找的名字： ")

for every_name in name_list:
    if every_name["name"] == find_name:
        print("找到了 %s" % find_name)
        print(every_name)
        break
else:
    print("没找到 %s" % find_name)