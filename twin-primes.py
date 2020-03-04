#!/usr/bin/env python3

## loads in primes.txt to a list and then looks for twin primes
## will then write to twin-primes.txt

from datetime import datetime

# initialize time to show elapsed time when script quits
startTime = datetime.now()

# function to get neighborhood of list item
# courtesy https://stackoverflow.com/questions/323750/how-to-access-the-previous-next-element-in-a-for-loop
def neighborhood(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)

# import primes.txt into primes[] list
try:
    with open('primes.txt', 'r') as file:
        primes = file.readlines()
except:
    print('primes.txt not found')

# cycle through primes[] and check for twin primes
count = 0
try:
    for prev, prime, next in neighborhood(primes):
        prime = int(prime)
        try:
            next = int(next)
        except:
            break
        if next - prime == 2:
            line = str(prime) + ', ' + str(next)
            print(line)
            with open('twin-primes.txt', 'a+') as file:
                file.write(line + '\n')
            count = count + 1

except KeyboardInterrupt:
    pass

# script complete
elapsedTime = datetime.now() - startTime
print('\n\nScript ran for %s and found %s pairs of twin primes.' % (str(elapsedTime), str(count)))
print('\nprimes.txt complete')
input()
