# Open the input file
file = open("input.txt", "r")
# Parse lines
data = [x.strip() for x in file.readlines()]

def part1(data):
    valid_passport_count = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    current = 0
    for line in data:
        if line == " ":
            if current == len(required_fields):
                valid_passport_count += 1

            current = 0
            continue

    for field in line.split():
        key, val = field.split(":")
        if key in required_fields:
            current += 1

    return valid_passport_count

print(f"Solution Part 1: {part1(data)}")