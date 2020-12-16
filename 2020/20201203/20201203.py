import os
current_folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_folder, '20201203.txt')

def collect_data():
    with open(data_file, 'r') as file:
        for line in file:
            yield line.rstrip()

def slope_counter(movement_right, movement_down):
    counter = 0
    horizontal_position = 0
    vertical_position = 0
    layers = list(collect_data())
    slope_length = len(layers)
    slice_length = len(layers[0])

    for slice in range(slope_length - 1):
        horizontal_position += movement_right
        vertical_position += movement_down

        if horizontal_position >= slice_length:
            horizontal_position = horizontal_position - slice_length

        if layers[vertical_position][horizontal_position] == '#':
            counter += 1
    return counter

def updated_slope_counter(movement_right, movement_down):
    counter = 0
    horizontal_position = 0
    vertical_position = 0
    layers = list(collect_data())
    slope_length = len(layers)
    slice_length = len(layers[0])

    for slice in range((slope_length - 1) / movement_down):
        horizontal_position += movement_right
        vertical_position += movement_down

        if horizontal_position >= slice_length:
            horizontal_position = horizontal_position - slice_length

        if layers[vertical_position][horizontal_position] == '#':
            counter += 1
    return counter

    
def runner():
    first_counter = slope_counter(1,1)
    print 'first_counter', first_counter
    second_counter = slope_counter(3,1)
    print 'second_counter', second_counter
    third_counter = slope_counter(5,1)
    print 'third_counter', third_counter
    fourth_counter = slope_counter(7,1)
    print 'fourth_counter', fourth_counter
    fifth_counter = updated_slope_counter(1,2)
    print 'fifth_counter', fifth_counter
    
    return first_counter * second_counter * third_counter * fourth_counter * fifth_counter

print runner()