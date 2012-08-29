max_bound = 10000000
nums = list(range(3, max_bound + 1, 2))
lnums = len(nums)
for n in range(lnums):
    if not nums[n]:
        continue
    next_prime = nums[n]
    i = n + next_prime
    while i < lnums:
        nums[i] = 0
        i += next_prime

primes = [ x for x in nums if x ] + [2]
