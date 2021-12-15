# --- Day 9: Smoke Basin ---
from collections import deque

input_path = r"day09input.txt"
with open(input_path, "r") as file:
    heightmap = []
    for line in file:
        heightmap.append([int(x) for x in line.strip()])

# Part one
def is_lower_point(x, y, map):
    adjacents = [     
                      [x, y-1], 
                [x-1, y],     [x+1, y], 
                      [x, y+1]
                ]
    lower_adjacents = 0
    total_adjacents = 0
    point_height = map[y][x]
    for coordinates in adjacents:
        new_x = coordinates[0]
        new_y = coordinates[1]
        if (0 <= new_x <= len(map[0]) - 1) and (0 <= new_y <= len(map) - 1):
            total_adjacents += 1
            if (point_height < map[new_y][new_x] ):
                lower_adjacents += 1
    
    if (lower_adjacents == total_adjacents):
        return True
    return False

lowest_points = [] # Used for starting part two.
risk_level = 0
for y_value in range(len(heightmap)):
    for x_value in range(len(heightmap[0])):
        if is_lower_point(x_value, y_value, heightmap):
            lowest_points.append((x_value, y_value))
            risk_level += (heightmap[y_value][x_value] + 1)
print(f"Part one -> Risk Level = {risk_level}")

# Part two
# Flood Fill - Help used for this part: https://www.youtube.com/watch?v=5Bochyn8MMI 
basins_sizes = []

def get_adjacents(x, y, map):
    adjacents = [     
                      [x, y-1], 
                [x-1, y],     [x+1, y], 
                      [x, y+1]
                ]
    valid_adjacents = []
    for coordinates in adjacents:
        new_x = coordinates[0]
        new_y = coordinates[1]
        if (0 <= new_x <= len(map[0]) - 1) and (0 <= new_y <= len(map) - 1):
            valid_adjacents.append((new_x, new_y))
    return valid_adjacents

def find_basin_size(map, start_point):
    queue = deque()
    queue.appendleft(start_point)
    visited_points = set()

    while len(queue) > 0:
        current_point = queue.pop()
        if current_point in visited_points:
            continue
        else:
            x_coord = current_point[0]
            y_coord = current_point[1]
            current_height = map[y_coord][x_coord]
            if current_height < 9:
                visited_points.add(current_point)
                for adjacent in get_adjacents(x_coord, y_coord, map):
                    queue.appendleft(adjacent) 

    return len(visited_points)

for point in lowest_points:
    size = find_basin_size(heightmap, point)
    basins_sizes.append(size)

basins_sizes.sort()
part_two_result = basins_sizes[-1] * basins_sizes[-2] * basins_sizes[-3]
print(f"Part two -> Product of three biggest basins = {part_two_result}")