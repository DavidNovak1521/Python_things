import re

data_file = open("data.txt", "r")
clean_data_file = open("clean_data.txt", "w")
value_frequency_file = open("value_frequency.txt", "w")
zero_frequency_file = open("zero_frequency.txt", "w")
dart_data_file = open("data.dart", "w")

data_count = 0
data_set = set()
max_value = 0
value_frequency = {}
values = {
    'a': 1,
    'á': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'é': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'í': 9,
    'j': 1,
    'k': 2,
    'l': 3,
    'm': 4,
    'n': 5,
    'o': 6,
    'ó': 6,
    'ö': 6,
    'ő': 6,
    'p': 7,
    'q': 8,
    'r': 9,
    's': 1,
    't': 2,
    'u': 3,
    'ú': 3,
    'ü': 3,
    'ű': 3,
    'v': 4,
    'w': 5,
    'x': 6,
    'y': 7,
    'z': 8,
  }

def line_not_empty(line):
    return line.strip() != ""

def clean_line(line):
    return line.strip().replace("\\", "\\\\").replace("'", "\\'")

def return_clean_line(line, value):
    return f"{value:<4} - {line}\n"

def return_dart_line(line, value):
    return f"    ('{line}', {value}),\n"

def calculate_value(input_text):
    temp_value = 0

    regex = re.compile(r'\d+')

    numbers = [
        int(number.group(0) or '0')
        for number in regex.finditer(input_text)
    ]

    if numbers:
        temp_value += sum(numbers)

    for char in input_text:
        if char.lower() in values:
            temp_value += values[char.lower()]

    return temp_value

dart_data_file.write("class AppData {\n  static const valuePairs = [\n")

for line in data_file:
    if line_not_empty(line):
        cleaned_line = clean_line(line)
        current_value = calculate_value(cleaned_line)

        if current_value > 0 and cleaned_line not in data_set:
            if current_value > max_value: max_value = current_value

            data_count += 1
            data_set.add(cleaned_line)

            if current_value in value_frequency: value_frequency[current_value] += 1
            else: value_frequency[current_value] = 1
            
            clean_data_file.write(return_clean_line(cleaned_line, current_value))
            dart_data_file.write(return_dart_line(cleaned_line, current_value))

dart_data_file.write("  ];\n}\n")

value_frequency = {item: value_frequency[item] for item in sorted(value_frequency.keys())}

for value in value_frequency:
    value_frequency_file.write(f'value: {value:<4}  -  frequency: {value_frequency[value]}\n')

zero_frequency_file.write('Zero frequency\n')
for i in range(1, max_value + 1):
    if i not in value_frequency:
        zero_frequency_file.write(f'value: {i}\n')

data_file.close()
clean_data_file.close()
value_frequency_file.close()
zero_frequency_file.close()
dart_data_file.close()

print('Files generated.')
print(f'Data count: {data_count}')
print(f'Maximum value: {max_value}')