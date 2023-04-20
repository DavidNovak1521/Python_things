# Smallest multiple
# 232792560
# 35s Macbook Air M1

import time

start = time.time()
top = 20
answer = top

def is_divisible(n):
    for i in range(top, 0, -1):
        if n % i != 0:
            return False
    return True

while True:
    if is_divisible(answer):
        break
    answer += 1

end = time.time()
print(f"{int(end - start)}s")
print(answer)