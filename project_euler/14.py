# Longest Collatz sequence
# 837799
# 14s Macbook Air M1

import time

start = time.time()

under_num = 1000000
current_length = 0
longest = 0
answer = 0

def next_number(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def chain_length(n):
    length = 1
    while (n > 1):
        n = next_number(n)
        length += 1
    
    return length

for i in range(1, under_num):
    current_length = chain_length(i)

    if current_length > longest:
        longest = current_length
        answer = i

end = time.time()
print(f"{int(end - start)}s")

print(answer)