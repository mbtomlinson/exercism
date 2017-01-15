def sieve(n):
    primes = [2]
    composites = []
    sieve_range = range(3,n+1)
    for num in sieve_range:
        for prime in primes:
            if num % prime == 0:
                composites.append(num)
        if num not in composites:
            primes.append(num)
    return primes
