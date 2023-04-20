# Even Fibonacci numbers
# 4613732

num1 = 1
num2 = 2
num3 = 4000000
sum = 0

while num2 < num3:
    if num2 % 2 == 0:
        sum += num2
    num1, num2 = num2, num1 + num2

print(sum)