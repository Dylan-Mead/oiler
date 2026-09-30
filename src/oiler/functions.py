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


def is_truncatable_prime(n, primes):

    str_n = str(n)
    if (set(str_n) & set('0468')):
        return False
    for i in range(1, len(str_n)):
        if int(str_n[i:]) not in primes or int(str_n[:i]) not in primes:
            return False
    return True

def string_is_palindrome(s):
    return s == s[::-1]

def find_curious_numbers(curious_numbers):
    from math import factorial
    start = max(curious_numbers, default=10) + 1
    for i in range(start, 3628800):
        digits = [int(d) for d in str(i)]
        digit_sum = 0
        for digit in digits:
            digit_sum += factorial(digit)
        if digit_sum == i:
            curious_numbers.append(i)
    return curious_numbers

def simplify(num, den):
    from math import gcd
    common_divisor = gcd(num, den)
    return num // common_divisor, den // common_divisor

def is_pandigital(n):
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = str(n)
    return len(s) == 9 and all(str(d) in s for d in digits)


def pandigital_products():
    products = set()
    for a in range(1, 100):
        for b in range(a, 10000):
            c = a * b
            if is_pandigital(f"{a}{b}{c}"):
                products.add(c)
    return products

def count_ways_to_make_change(principle, coins):
    ways = [0] * (principle + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, principle + 1):
            ways[i] += ways[i - coin]
    return ways[principle]

def sum_diagonals_0f_square(size: int) -> int:
    if size % 2 == 0:
        raise ValueError("Size must be an odd number")
    if size == 1:
        return 1
    return 4 * size * size - 6 * size + 6 + sum_diagonals_0f_square(size - 2)