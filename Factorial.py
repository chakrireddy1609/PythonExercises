def factorial_rec(num):
    fact = 1
    if num <= 1:
        return 1
    for i in range(1, num+1):
        fact = num * factorial_rec(i-1)
    return fact


def factorial_iter(num):
    fact = 1
    for i in range(num, 0, -1):
        fact *= i
    return fact


print(factorial_rec(6))
print(factorial_iter(6))