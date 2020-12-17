import os
current_folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_folder, '20201204.txt')

def collect_data():
    outer_list = []
    inner_list = []
    with open(data_file, 'r') as file:
        for line in file:
            if line.rstrip() == '':
                outer_list.append(inner_list)
                inner_list = []
            else:
                for el in line.rstrip().split(' '):
                    inner_list.append(el.split(':')[0])
    return outer_list
    


def runner():
    passport_count = 0
    REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    pass_port_list = collect_data()
    for passport in pass_port_list:
        for required_field in REQUIRED_FIELDS:
            if required_field not in passport:
                passport_count += 1
                break
    return len(pass_port_list) - passport_count
            

print runner()
