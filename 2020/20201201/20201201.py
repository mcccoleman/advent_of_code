import os
current_folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_folder, '20201201.txt')

def collect_data():
    with open(data_file, 'r') as file:
        for line in file:
            yield int(line.rstrip())


def runner():
    # part one
    # numbers = list(collect_data())
    # num_length = len(numbers)
    # for x in range(num_length):
    #     for y in range(num_length):
    #         if numbers[x] + numbers[y] == 2020:
    #             print numbers[x] * numbers[y]
    #             return

    # part two
    numbers = list(collect_data())
    num_length = len(numbers)
    for x in range(num_length):
        for y in range(num_length):
            for w in range(num_length):
                if numbers[x] + numbers[y] + numbers[w] == 2020:
                    print numbers[x] * numbers[y] * numbers[w]
                    return


runner()