#!/usr/bin/env python3

## generates the first 100,000 prime numbers and returns script
## run time when complete

from math import sqrt
from datetime import datetime

# initialize time to show elapsed time when quit
startTime = datetime.now()

# main loop
# initialize test number as last prime + 2
primes = [2, 3]
n = primes[-1] + 2
count = 2
try:
    while count < 100000:
        # check divisibility of n by all primes < sqrt(n)
        for prime in primes:
            if prime <= sqrt(float(n)):
                if n % prime == 0:
                    # n is not prime
                    n = n + 2
                    break
            else:
                # n is prime because it is not divisible by any primes less than
                # the square root of n (relatively easy to prove)
                print(str(n))
                primes.append(n)
                n = n + 2
                count = count + 1
                break
except KeyboardInterrupt:
    elapsedTime = datetime.now() - startTime
    print('\n\nScript ran for %s and found %s primes.' % (str(elapsedTime), str(count)))

elapsedTime = datetime.now() - startTime
print('\n\nScript ran for %s and found %s primes.' % (str(elapsedTime), str(count)))
