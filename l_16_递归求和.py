def sum_num(num):

    if num == 1:

        return 1

    sum_n = num + sum_num(num - 1)

    return sum_n


result = sum_num(3)

print(result)
