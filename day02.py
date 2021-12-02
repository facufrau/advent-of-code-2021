# --- Day 2: Dive! ---
input_path = r"E:\Facundo\003-Programación\advent-of-code-2021\day02input.txt";

def process_input(path_string):
    with open(path_string, "r") as file:
        commands_array = [[x[:-3], int(x[-3:])] for x in file.readlines()]
    return commands_array
commands_array = process_input(input_path)

# PART ONE
coordinates = {'x': 0, 'y': 0}
for command in commands_array:
    if (command[0] == 'forward'):
        coordinates['x'] += command[1]
    elif (command[0] == 'up'):
        coordinates['y'] -= command[1]
    elif (command[0] == 'down'):
        coordinates['y'] += command[1]
print(f"Part one answer -> {coordinates['x'] * coordinates['y']}")

# PART TWO
coordinates = {'x': 0, 'y': 0, 'aim': 0}
for command in commands_array:
    if (command[0] == 'forward'):
        coordinates['x'] += command[1]
        coordinates['y'] += coordinates['aim'] * command[1]
    elif (command[0] == 'up'):
        coordinates['aim'] -= command[1]
    elif (command[0] == 'down'):
        coordinates['aim'] += command[1]
print(f"Part two answer -> {coordinates['x'] * coordinates['y']}")