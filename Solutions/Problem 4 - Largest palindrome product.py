"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 91 x 99 = 9009

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(n):
  n = str(n)
  return n == n[::-1]

def largest_palindrome(n):
  max_palindrome = 0
  for x in range(10 ** (n - 1), 10 ** n):
    for y in range(x, 10 ** n):
      product = x * y
      if isPalindrome(product):
        max_palindrome = max(product, max_palindrome)
  
  return max_palindrome