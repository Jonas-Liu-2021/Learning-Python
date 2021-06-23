def print_sum(num):

    print(num)

    if num == 1:

        return

    print_sum(num-1)

print_sum(3)