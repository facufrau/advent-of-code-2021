# --- Day 8: Seven Segment Search ---
input_path = r"day08input.txt"

# Part one
with open(input_path, "r") as file:
    output_values = []
    for line in file:
        output_values += line.split(' | ')[1].replace('\n', '').split(' ')

unique_numbers_counter = len([x for x in output_values if len(x) in [2,3,4,7]])
print(f"Part one -> Amount of 1,4,7,8 digits: {unique_numbers_counter}")

# Part two
def decode(signal):
    # Decodes signals and returns a dictionary with values.
    decoder_dict = {}
    encoder_dict = {}

    for index in [0,1,2,9]:
        if index == 0:
            decoder_dict[signal[index]] = 1
            encoder_dict[1] = signal[index]
        elif index == 1:
            decoder_dict[signal[index]] = 7
            encoder_dict[7] = signal[index]
        elif index == 2:
            decoder_dict[signal[index]] = 4
            encoder_dict[4] = signal[index]
        elif index == 9:
            decoder_dict[signal[index]] = 8
            encoder_dict[8] = signal[index]
    
    for item in signal:
        if (len(item) == 5):
            if (set(encoder_dict[1]) <= set(item)):
                decoder_dict[item] = 3
            elif (len(set(encoder_dict[4]) - set(item)) == 1):
                decoder_dict[item] = 5
            else:
                decoder_dict[item] = 2           
        elif (len(item) == 6):
            if (not set(encoder_dict[1]) <= set(item)):
                decoder_dict[item] = 6
            elif (len(set(item) - set(encoder_dict[4])) == 2):
                decoder_dict[item] = 9 
            else:
                decoder_dict[item] = 0
    return decoder_dict


with open(input_path, "r") as file:
    signals, output_values = [], []
    for line in file:
        line_with_signals_sorted = [''.join(sorted(x)) for x in line.split(' | ')[0].split()]
        signals.append(sorted(line_with_signals_sorted, key=len))

        line_with_output_sorted = [''.join(sorted(x)) for x in line.split(' | ')[1].replace('\n', '').split()]
        output_values.append(line_with_output_sorted)

total_sum_of_output = 0
for signal, output in zip(signals, output_values):
    decoder = decode(signal)
    decoded_output = "".join([str(decoder[x]) for x in output])
    total_sum_of_output += int(decoded_output)

print(f"Part two -> Adding all output values: {total_sum_of_output}")
