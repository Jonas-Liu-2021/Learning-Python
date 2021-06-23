unit_price = input("请输入单价/元： ")

weight = input("请输入购买的苹果质量/千克： ")

total_price = float(unit_price) * float(weight)

print(str(total_price) + "元")