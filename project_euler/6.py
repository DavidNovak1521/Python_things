# Sum square difference
# 25164150

amount = 100

def sum_of_the_squares(n):
    return sum(i**2 for i in range(1, n+1))

def square_of_the_sum(n):
    return sum(i for i in range(1, n+1))**2

print(square_of_the_sum(amount) - sum_of_the_squares(amount))