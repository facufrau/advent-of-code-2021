# --- Day 6: Lanternfish ---

input_path = r"day06input.txt"
with open(input_path, "r") as file:
    fish_timers_array = sorted([int(x) for x in file.read().split(',')])
    fish_timers_array = [fish_timers_array.count(x) for x in range(9)]

def calculate_fish_amount(days, timers):
    for i in range(days):
        fish_with_timer_zero = timers[0]
        fish_with_timer_six = timers[7] + fish_with_timer_zero
        timers = timers[1:7]  + [fish_with_timer_six] + [timers[8]] + [fish_with_timer_zero]
    return sum(timers)

part_one = calculate_fish_amount(80, fish_timers_array)
print(f"Part one -> {part_one} lanternfish")
part_two = calculate_fish_amount(256, fish_timers_array)
print(f"Part two -> {part_two} lanternfish")
