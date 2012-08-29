import time
min_bound, max_bound = map(int, raw_input('Enter the bounds: ').split())

primes = [2]
differences = []
nums = range(3, max_bound + 1, 2)
while nums:
    next_prime = nums.pop(0)
    nums = filter(lambda x: x%next_prime != 0, nums)
    differences.append(next_prime - primes[-1])
    primes.append(next_prime)

found = False
while not found:
    little_index = differences.index(max(differences))
    if primes[little_index] < min_bound:
        primes = primes[little_index+1:]
        differences = differences[little_index+1:]
    else:
        found = True

print primes[little_index], primes[little_index + 1]