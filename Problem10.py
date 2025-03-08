# Problem 10 - Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from NumberTests import isPrime

def sumOfPrimes(limit):
    """Returns the sum of all prime numbers below the given limit"""
    total = 0
    for num in range(2, limit):
        if isPrime(num):
            total += num
    return total


result = sumOfPrimes(2000000)
print("Sum of all primes below two million:", result)