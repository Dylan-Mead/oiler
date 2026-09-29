from math import sqrt

import os

with open(os.path.join(os.path.dirname(__file__), "primes.txt")) as f:
    primes = [int(line.strip()) for line in f]

def factor_generator(primes, number):
    #first we set a ceiling because a prime factor can never be larger than the square root of the number
    ceiling = int(sqrt(number))
    # we start checking for prime factors from the largest known prime plus 2
    candidate = primes[-1] + 2
    # this will hold the prime factors we find
    factors = []
    # first we try dividing by the known primes and remove their multiples from the number
    for prime in primes:
        if number % prime == 0:
            factors.append(prime)
            while number % prime == 0:
                number //= prime
            ceiling = int(sqrt(number))
            if number == 1:
                return factors, primes
    # now we check for prime factors larger than the known primes
    while number > 1:
        #check candidate against known primes to determine if it is a prime itself
        if candidate > ceiling:
            factors.append(number)
            primes#.append(number)
            return factors, primes
        is_prime = all(candidate % p != 0 for p in primes if p <= sqrt(candidate))
        if is_prime:
            primes.append(candidate)
            if number % candidate == 0:
                factors.append(candidate)
                while number % candidate == 0:
                    number //= candidate
                ceiling = int(sqrt(number))
        candidate += 2
    return factors, primes

def primes_generator(primes, prime_count):
    candidate = primes[-1] + 2
    ceiling = int(sqrt(candidate))
    while True:
        is_prime = True
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
            if prime > ceiling:
                break
        if is_prime:
            primes.append(candidate)
            #yield candidate
            if len(primes) >= prime_count:
                return primes
        candidate += 2
        ceiling = int(sqrt(candidate))


def primes_max(primes, min_value):
    while primes[-1] < min_value:
        primes = primes_generator(primes, len(primes) + 1)
    return primes

def count_prime_factors(n, primes=primes):
    primes_factors = []
    #count = 1
    for p in primes:
        if n % p == 0:
            #count += 1
            primes_factors.append(p)
            while n % p == 0:
                n //= p
        if n == 1:
            break
    return len(primes_factors), primes_factors

def find_divisors(n: int):
    divisors = []
    # Loop from 1 up to the square root of n
    i = 1
    #ceiling = int(n**0.5)
    while i * i <= n:#<= ceiling:
        if n % i == 0:
            divisors.append(i)      # Add the smaller divisor
            # Add the paired divisor if it's distinct (handles perfect squares)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    divisors.sort() 
    return len(divisors), divisors


