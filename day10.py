# --- Day 10: Syntax Scoring ---
input_path = r"day10input.txt"
with open(input_path, "r") as file:
    lines = file.read().split('\n')

# Part one
scores_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
matches = {"(": ")", "[": "]", "{": "}", "<": ">"}
opening_chars = ["(", "[", "{", "<"]

total_error_points = 0
chars_for_completion = []
for line in lines:
    open_chars = []
    has_error = False
    for char in line:
        if char in opening_chars:
            open_chars.append(char)
        else:
            current = open_chars.pop()
            if (char == matches[current]):
                continue
            else:
                total_error_points += scores_map[char]
                has_error = True
                break
    
    # Preparing data for part two
    if (not has_error):
        chars_for_completion.append([matches[x] for x in reversed(open_chars)])
print(f"Part one -> Total error points: {total_error_points}")

# Part two
completion_scores_map = {")": 1, "]": 2, "}": 3, ">": 4}
scores = []
for line in chars_for_completion:
    line_score = 0
    for c in line:
        line_score = (line_score * 5) + completion_scores_map[c]
    scores.append(line_score)
scores.sort()
print(f"Part two -> Middle completion score: {scores[len(scores) // 2]}")