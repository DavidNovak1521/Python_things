# Lattice Paths
# 137846528820
# combination formula: n! / (k! * (n - k)!)

x = 20

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def formula(x):
    return factorial(2*x) / (factorial(x) * factorial(x))

print(int(formula(x)))