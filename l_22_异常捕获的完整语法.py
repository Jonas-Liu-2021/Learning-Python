try:
    num = int(input("请输入一个整数： "))
    division_num = 8 / num
except ZeroDivisionError:
    print("除数不能为0")
except Exception as result:
    print("其他错误 %s" % result)
else:
    print("一切正常")
finally:
    print('程序结束')

print("*" * 50 )
