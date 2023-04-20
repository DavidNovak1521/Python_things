# 10001st prime
# 104743

num = 10001
prime = 1

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

for i in range(num):
    prime = next_prime(prime)

print(prime)