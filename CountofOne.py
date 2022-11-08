def countOfOne(num):
    one_sum = 0
    bin_num = bin(num)[2:]
    for i in bin_num:
        one_sum += int(i)
    return one_sum

print(countOfOne(11))

