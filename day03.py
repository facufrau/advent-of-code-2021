# --- Day 3: Binary Diagnostic ---
from collections import Counter

input_path = r"E:\Facundo\003-Programación\advent-of-code-2021\day03input.txt"
NUMBER_LENGTH = 12

# PART ONE
with open(input_path, "r") as file:
    string_of_bits = file.read().replace('\n','')

digit_string_list = []
for order in range(NUMBER_LENGTH):
    column_of_bits = ""
    for i in range(order, len(string_of_bits), NUMBER_LENGTH):
        column_of_bits += string_of_bits[i]
    digit_string_list.append(column_of_bits)

most_common_bits = ""
least_common_bits = ""
for item in digit_string_list:
    bit_counter = Counter(item).most_common(2)
    most_common_bits += bit_counter[0][0]
    least_common_bits += bit_counter[1][0]

print(f"Part one answer -> {int(most_common_bits,2) * int(least_common_bits,2)}")

# PART TWO
with open(input_path, "r") as file:
    list_of_numbers = file.read().splitlines()

oxygen_rating = list_of_numbers[:]
dioxide_rating = list_of_numbers[:]

def find_most_least_common(option, order, numbers):
    numbers_string = "".join(numbers)
    filtered_string = ""
    for i in range(order, len(numbers_string), NUMBER_LENGTH):
        filtered_string += numbers_string[i]
    
    bit_counter = Counter(filtered_string).most_common(2)
    if option == "most":
        if (len(bit_counter) == 1):
            return bit_counter[0][0]
        elif (bit_counter[0][1] == bit_counter[1][1]):
            return '1'
        return bit_counter[0][0]
    elif option == "least":
        if (len(bit_counter) == 1):
            return bit_counter[0][0]
        elif (bit_counter[1][1] == bit_counter[0][1]):
            return '0'
        return bit_counter[1][0]


order = 0
while (len(oxygen_rating) > 1):
    most_common = find_most_least_common("most", order, oxygen_rating)
    temporary = []
    for number in oxygen_rating:
        if number[order] == most_common:
            temporary.append(number)
    oxygen_rating = temporary
    order += 1

order = 0
while (len(dioxide_rating) > 1):
    least_common = find_most_least_common("least", order, dioxide_rating)
    temporary = []
    for number in dioxide_rating:
        if number[order] == least_common:
            temporary.append(number)
    dioxide_rating = temporary
    order += 1

result = int(oxygen_rating[0], 2) * int(dioxide_rating[0], 2)
print(f"Part two answer -> {result}")