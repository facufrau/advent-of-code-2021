# --- Day 1: Sonar Sweep ---

input_path = r"E:\Facundo\003-Programación\advent-of-code-2021\day01input.txt";

def process_input(path_string):
    with open(path_string, "r") as file:
        depths_array = [int(x) for x in file.readlines()]
    return depths_array

# PART ONE
depths_array = process_input(input_path)
increases_counter = 0
for i, depth in enumerate(depths_array):
    if (i == 0):
        continue
    elif (depth > depths_array[i-1]):
        increases_counter += 1

print(f"Part one answer - Measurement increases: {increases_counter}")
    
# PART TWO
increases_counter = 0
for i in range(len(depths_array)):
    group_of_three = depths_array[i:i+3]
    if (i == 0):
        current_group_sum = sum(group_of_three)
    elif (len(group_of_three) == 3):
        previous_group_sum = current_group_sum
        current_group_sum = sum(group_of_three)
        if (current_group_sum > previous_group_sum):
            increases_counter += 1

print(f"Part two answer - Measurement increases: {increases_counter}")