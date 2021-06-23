def print_line(char, times):
    """打印多个字符

    :param char: 字符
    :param times:打印数量
    """
    print(char * times)


def print_lines(char, times):
    """打印多行符号

    :param char: 字符
    :param times: 打印行数
    """
    row = 0
    while row < times:
        print_line(char, times)
        row += 1


name = "奥秘法"
