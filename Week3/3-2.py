import time
min_bound, max_bound = map(int, raw_input('Enter the bounds: ').split())
start = time.time()
primes = [2]
differences = []
nums = range(3, max_bound + 1, 2)
for n in xrange(len(nums)):
    if not nums[n]:
        continue
    next_prime = nums[n]
    i = n + next_prime
    while i < len(nums):
        nums[i] = 0
        i += next_prime
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

print time.time()-start
print primes[little_index], primes[little_index + 1]