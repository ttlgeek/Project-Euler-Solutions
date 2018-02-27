"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatzSequenceLength(start):
  curr_number = start
  length = 1
  while curr_number != 1:
    if curr_number % 2 == 0:
      curr_number /= 2
    else:
      curr_number = 3 * curr_number + 1
    length += 1
  
  return length

def longestChain(limit):
  maxChainLength = 0
  maxNumber = 0
  for i in range(1, limit + 1):
    chainLength = collatzSequenceLength(i)
    if chainLength > maxChainLength:
      maxNumber = i
      maxChainLength = chainLength
  
  return maxNumber