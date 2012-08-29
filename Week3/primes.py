import timeit
from time import time
max_bound = 10000000
repetitions = 1000
start_chop = 0
print_results = False

def primes(max_bound):
    nums = range(3, max_bound + 1, 2)
    lnums = len(nums)
    for n in xrange(int(lnums**0.5)):
        if not nums[n]:
            continue
        next_prime = nums[n]
        nums[n + next_prime::next_prime] = (0,)*int((lnums-n-0.5)/next_prime)

    primes = [2] + [ x for x in nums if x ]

statement = 'primes(%s)' % max_bound
primetimer = timeit.Timer(statement,'from __main__ import primes')
result = primetimer.repeat(repetitions+start_chop,1)[start_chop:]
start_time = time()
primes(max_bound)
run_time = time() - start_time

print 'Min:', min(result)
print 'Max:', max(result)
print 'Avg:', sum(result)/len(result)
print
print 'Single run:', run_time
if print_results:
    print
    print '-----Incoming Results-----'
    print result

#Min: 1.1812210083
#Max: 1.81338906288
#Avg: 1.53763728833
