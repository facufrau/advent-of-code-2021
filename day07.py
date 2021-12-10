# --- Day 7: The Treachery of Whales ---

input_path = r"day07input.txt"
with open(input_path, "r") as file:
    positions = [int(x) for x in file.read().split(',')]
    max_variations = max(positions)

# Part one
fuel_costs = []
for i in range(max_variations):
    fuel_needed = sum([abs(x - i) for x in positions])
    fuel_costs.append(fuel_needed)
print(f"Part one -> Min fuel cost: {min(fuel_costs)}")

# Part two
fuel_costs = []
for i in range(max_variations):
    fuel_needed = sum([((abs(x-i)**2 + abs(x-i)) / 2) for x in positions])
    fuel_costs.append(fuel_needed)
print(f"Part two -> Min fuel cost: {int(min(fuel_costs))}")