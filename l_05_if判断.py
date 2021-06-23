gpa = float(input("请输入您的GPA： "))

if gpa > 90:
    print("优秀")
elif gpa > 80:
    print("良好")
elif gpa > 70:
    print("一般")
elif gpa > 60:
    print("及格")
else:
    print("不及格")
