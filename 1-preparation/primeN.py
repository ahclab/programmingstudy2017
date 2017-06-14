#! python
import sys

upper = int(sys.argv[1])

primes = []

for x in range(upper):
    number = x + 1
    flag = 0
    if number != 1:
        for prime in primes:
            if number % prime == 0:
                flag = 1
        if flag == 0:        
            primes.append(number)
    
print len(primes)
    

