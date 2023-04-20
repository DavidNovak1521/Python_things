# Largest prime factor
# 6857

num = 600851475143
current_prime = 2

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    # return n != 1

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

while num > 1:
    if num % current_prime == 0:
        num /= current_prime
    else:
        current_prime = next_prime(current_prime)

print(current_prime)