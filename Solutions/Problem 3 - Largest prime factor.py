"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

def getFactors(n):
  factors = []
  for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
      factors.append(i)
      factors.append(n // i)
  return factors

def isPrime(n):
  return len(getFactors(n)) == 2

def largest_prime_factor(n):
  max_factor = 0
  factors = getFactors(n)
  for i in factors:
    if isPrime(i):
      max_factor = max(max_factor, i)
  return max_factor