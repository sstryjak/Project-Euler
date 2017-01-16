# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

prime_factors = list()

def FindPrimeFactors(target_num, current_smallest_prime):
    # print(target_num)
    # print (target_num, current_smallest_prime)
    while (current_smallest_prime <= target_num):

        if (current_smallest_prime == target_num):
            prime_factors.append(current_smallest_prime)
            break
        elif (target_num % current_smallest_prime == 0):
            prime_factors.append(current_smallest_prime)
            target_num = target_num / current_smallest_prime
        else:
            current_smallest_prime = current_smallest_prime + 1
            FindPrimeFactors(target_num, current_smallest_prime)

    # print(target_num)


FindPrimeFactors(18, 2)
print(prime_factors)
