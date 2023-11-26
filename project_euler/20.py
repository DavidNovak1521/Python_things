# Factorial Digit Sum
# 648

num = 100

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def sum_of_digits(n):
    return sum([int(d) for d in str(n)])

print(factorial(num))
print(sum_of_digits(factorial(num)))