import os
current_folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_folder, '20201204.txt')

def collect_data():
    outer_list = []
    inner_list = {}
    with open(data_file, 'r') as file:
        for line in file:
            if line.rstrip() == '':
                outer_list.append(inner_list)
                inner_list = {}
            else:
                for el in line.rstrip().split(' '):
                    inner_list[el.split(':')[0]] = el.split(':')[1]
    return outer_list



def possesses_invalid_attributes(passport):
    REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for required_field in REQUIRED_FIELDS:
        if required_field not in passport:
            return True
    return False



def birth_year_valid(str):
    return len(str) == 4 and int(str) >= 1920 and int(str) <= 2020

def issue_year_valid(str):
    return len(str) == 4 and int(str) >= 2010 and int(str) <= 2020

def expiration_year_valid(str):
    return len(str) == 4 and int(str) >= 2020 and int(str) <= 2030

def height_valid(str):
    if 'cm' in str or 'in' in str:
        if 'cm' in str:
            return int(str.replace('cm', '')) < 193 and int(str.replace('cm', '')) > 150
        elif 'in' in str:
            return int(str.replace('in', '')) < 76 and int(str.replace('in', '')) > 59
        return False
    return False

def valid_hair_color(str):
    if '#' not in str:
        return False
    if len(str.split("#")[1]) != 6:
        return False
    return True

def valid_eye_color(str):
    return str in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_country(str):
    return len(str) == 9 and str.isdigit()
 

def runner():
    passport_count = 0
    pass_port_list = collect_data()
    for passport in pass_port_list:
        if possesses_invalid_attributes(passport) or not birth_year_valid(passport['byr']) or not issue_year_valid(passport['iyr']) or not expiration_year_valid(passport['eyr']) or not height_valid(passport['hgt']) or not valid_hair_color(passport['hcl']) or not valid_eye_color(passport['ecl']) or not valid_country(passport['pid']):
            passport_count += 1
        
    print passport_count
    return len(pass_port_list) - passport_count
            

runner()
