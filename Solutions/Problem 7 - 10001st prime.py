"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

def nth_prime(n):
  i = 2
  curr_prime = 1
  prime_count = 1
  while prime_count <= n:
    if isPrime(i):
      prime_count += 1
      curr_prime = i
    i += 1
  return curr_prime