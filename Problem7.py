# Problem 7 - 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?


from NumberTests import isPrime

def main():
    n = int(input("Enter the position of the prime number to find: "))
    print(f"The {n}th prime number is:", findNthPrime(n))

def findNthPrime(n):
    """Finds the nth prime number"""
    prime = 0
    count = 0
    num = 1
    while count < n:
        num += 1
        if isPrime(num):
            count += 1
            prime = num
    return prime

if __name__ == '__main__':
    main()