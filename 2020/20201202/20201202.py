import os
current_folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_folder, '20201202.txt')

def collect_data():
    with open(data_file, 'r') as file:
        for line in file:
            yield str(line.rstrip())


def capture_low_number(string):
    split = string.split(' ')
    return int(split[0].split('-')[0])

def capture_high_number(string):
    split = string.split(' ')
    return int(split[0].split('-')[1])

def capture_letter(string):
    split = string.split(' ')
    return split[1][0]

def capture_code(string):
    split = string.split(' ')
    return split[2]

def is_valid(string):
    low_number = capture_low_number(string)
    high_number = capture_high_number(string)
    letter = capture_letter(string)
    code = capture_code(string)
    num_appearing = code.count(letter)
    return num_appearing >= low_number and num_appearing <= high_number

def is_valid_pt_2(string):
    low_number = capture_low_number(string)
    high_number = capture_high_number(string)
    letter = capture_letter(string)
    code = capture_code(string)
    valid_low_number = code[low_number - 1] == letter
    valid_high_number = code[high_number - 1] == letter

    if valid_low_number and valid_high_number:
        return False
    if valid_low_number or valid_high_number:
        return True
    return False



def runner():
    count = 0
    codes = list(collect_data())
    for string in codes:
        # count += is_valid(string)
        count += is_valid_pt_2(string)
    return count

print runner()