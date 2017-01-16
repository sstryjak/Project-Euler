# https://projecteuler.net/
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

# multiples_found = list()

#
# for i in range(2,10):
#     if (i % 2 == 0):
#         running_total = running_total + i
#         print(i, running_total)


# print(running_total)

def fib(n):
    running_total = 0
    a, b = 0, 1
    while a < n:
        # print(a, end=' ')
        if (b % 2 == 0):
            running_total = running_total + b
        a, b = b, a+b
    print('\n')
    print(running_total)

fib(4000000)

