# --- Day 5: Hydrothermal Venture ---
from collections import Counter
from itertools import chain

input_path = "day05input.txt"
SIDE_LENGTH = 1000

def draw_map(length):
    map = []
    for i in range(length):
        row = []
        for j in range(length): 
            row.append(0)
        map.append(row)
    return map

def draw_line_vertical(start, end, map_array):
    y1, y2 = start[1], end[1]
    x = start[0]
    if y1 <= y2:
        for yi in range(y1, y2 + 1):
            map_array[yi][x] += 1
    else:
        for yi in range(y2, y1 + 1):
            map_array[yi][x] += 1

def draw_line_horizontal(start, end, map_array):
    x1, x2 = start[0], end[0]
    y = start[1]
    if x1 <= x2:
        for xi in range(x1, x2 + 1):
            map_array[y][xi] += 1
    else:
        for xi in range(x2, x1 + 1):
            map_array[y][xi] += 1

def draw_line_diagonal(start, end, map_array):
    x1, x2 = start[0], end[0]
    y1, y2 = start[1], end[1]
    if y1 < y2:
        for i in range((x2 - x1) + 1):
            map_array[y1+i][x1+i] += 1
    elif y1 > y2:
        for i in range((x2 - x1) + 1):
            map_array[y1-i][x1+i] += 1

def count_more_2_lines(map_array):
    counter = Counter(chain(*map_array))
    total = 0
    for key, value in counter.items():
        if key >= 2:
            total += value
    return total

map = draw_map(SIDE_LENGTH)
with open(input_path, "r") as file:
    lines = []
    for line in file:
        line = line.strip('\n').split(' -> ')
        start = tuple(int(x) for x in line[0].split(',')) 
        end = tuple(int(x) for x in line[1].split(','))
        lines.append([start, end])

        # Part one
        if (start[0] == end[0]):
            draw_line_vertical(start, end, map)
        elif (start[1] == end[1]):
            draw_line_horizontal(start, end, map)
    print(f"Part one result -> {count_more_2_lines(map)}")

# Part two
for line in lines:
    sorted_line = sorted(line , key=lambda k: [k[0], k[1]])
    start = sorted_line[0]
    end = sorted_line[1]
    if (start[0] != end[0]) and (start[1] != end[1]):
        draw_line_diagonal(start, end, map)
print(f"Part two result -> {count_more_2_lines(map)}")
