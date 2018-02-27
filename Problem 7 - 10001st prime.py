"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

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