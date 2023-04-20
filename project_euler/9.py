# Special Pythagorean triplet
# 31875000
# ugly

a = 0
b = 0
c = 0

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

for i in range(1, 998):
    for j in range(a, 998):
        if is_pythagorean_triplet(i, j, 1000-i-j):
            print(i, j, 1000-i-j)
            a = i
            b = j
            c = 1000-i-j
            break
    if a > 0:
        break

print(a*b*c)