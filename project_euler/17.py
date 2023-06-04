# Number Letter Counts
# 21124

from num2words import num2words

num = 1000
letter_counts = 0

def number_to_letter_count(n):
    words = num2words(n)
    clean_string = ''.join(char for char in words if char.isalpha())
    return len(clean_string)

# for i in range(1,num+1):
#     letter_counts += number_to_letter_count(i)

letter_counts = sum(number_to_letter_count(i) for i in range(1, num+1))

print(letter_counts)