# Amicable Numbers
# 31626

num = 10000
sum_of_amicables = 0

def sum_of_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

for i in range(num):
    j = sum_of_proper_divisors(i)
    if i == sum_of_proper_divisors(j) and i != j:
        sum_of_amicables += i

print(sum_of_amicables)