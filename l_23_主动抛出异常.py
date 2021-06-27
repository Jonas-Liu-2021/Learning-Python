def psw_setting():

    psw = input("请输入密码： ")

    if len(psw) >= 8:
        return psw

    error_type = Exception("您的密码长度不够")

    raise error_type


try:
    print(psw_setting())
except Exception as result:
    print(result)