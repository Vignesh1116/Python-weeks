# When an unbiased dice with 12 faces having the numbers from 1 to 12 is rolled, the probability of
# obtaining a prime number is . Set up a computational experiment to verify this.

import random

trials = 10000
prime_count = 0

primes = [2, 3, 5, 7, 11]

for i in range(trials): #9999
    dice = random.randint(1, 12) #5

    if dice in primes:
        prime_count += 1

probability = prime_count / trials

print("Experimental Probability:", probability)
