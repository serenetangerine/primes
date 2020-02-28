#!/usr/bin/env python3

from math import sqrt
from datetime import datetime

# initialize time to show elapsed time when quit
startTime = datetime.now()

# import primes.txt into primes[] list
try:
    with open('primes.txt', 'r') as file:
        primes = file.readlines()
except:
    # initialize primes.txt and primes[] list
    primes = [2, 3]
    with open('primes.txt', 'a+') as file
        for prime in primes:
            file.write(str(prime) + '\n')

# main loop
# initialize test number as last prime + 2
n = int(primes[-1]) + 2
count = 0
try:
    while True:
        # check divisibility of n by all primes < sqrt(n)
        for prime in primes:
            prime = int(prime)
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
                with open('primes.txt', 'a') as file:
                    file.write(str(n) + '\n')
                n = n + 2
                count = count + 1
                break
except KeyboardInterrupt:
    elapsedTime = datetime.now() - startTime
    print('\n\nScript ran for %s and found %s primes.' % (str(elapsedTime), str(count)))
