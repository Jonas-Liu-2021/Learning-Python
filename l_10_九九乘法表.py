i = 1

while i <= 9:
    m = 1
    while m <= i:
        print("%d * %d = %d" %(m, i, m * i), end="\t\t")
        m += 1
    print()
    i += 1