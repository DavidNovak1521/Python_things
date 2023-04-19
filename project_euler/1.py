# Multiples of 3 or 5
# 233168

num1 = 3
num2 = 5
num3 = 1000
sum = 0

for i in range(num3):
    if i % num1 == 0 or i % num2 == 0:
        sum += i

print(sum)
