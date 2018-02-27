"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

#It's slow, needs to be optimized

from math import sqrt

def getFactors(n):
  factors = 0
  for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
      factors += 1
  return factors

def isPrime(limit):
  return getFactors(limit) == 1


def primeSum(limit):
  prime_Sum = 0
  for i in range(2, limit):
    if isPrime(i):
      prime_Sum += i
  return prime_Sum

print(primeSum(2000000))