# Largest palindrome product
# 906609

digit = 3
palindrome = 0
num_pair = ()

def is_palindrome(n):
    return str(n) == str(n)[::-1]

for i in range(int('1'+'0'*(digit-1)), int('1'+'0'*digit)):
    for j in range(int('1'+'0'*(digit-1)), int('1'+'0'*digit)):
        if is_palindrome(i * j):
            if i * j > palindrome:
                palindrome = i * j
                num_pair = (i, j)

print(num_pair)
print(palindrome)