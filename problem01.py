# https://projecteuler.net/
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

multiples_found = list()

top_number = 1000
multiplier3 = 3
multiplier5 = 5
current_num = 1
running_total = 0

while current_num < top_number:
    if (current_num % multiplier3 == 0 or current_num % multiplier5 == 0):
        multiples_found.append(current_num)
        running_total = running_total + current_num
    current_num += 1

# print(multiples_found)
print(running_total)