# Summation of primes
# 142913828922
# 5s Macbook Air M1
# it needs to be speeded up

import time

start = time.time()

prime = 2
primes = []
num = 2000000

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

while prime < num:
    primes.append(prime)

    prime = next_prime(prime)

end = time.time()
print(f"{int(end - start)}s")

print(sum(primes))