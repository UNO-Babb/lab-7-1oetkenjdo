# Problem 4 - Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from NumberTests import isPalindrome

def main():
    print(largestPalindromeProduct())

def largestPalindromeProduct():
    """Finds the largest palindrome made from the product of two 3-digit numbers"""
    
    largest_palindrome = 0
    for i in range(999, 99, -1):
        for s in range(i, 99, -1):  
            product = i * s
            if product <= largest_palindrome:
                break
            if isPalindrome(product):
                largest_palindrome = product
    return largest_palindrome

if __name__ == '__main__':
    main()