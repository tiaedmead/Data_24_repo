def check_count(password, letter, start, stop):
    return start <= password.count(letter) <= stop


def check_indexes(password, letter, start, stop):
    return (password[start] == letter or password[stop] == letter) and (password[start] != password[stop])


with open("input.txt") as file:

    letters = [num.split(": ") for num in file]
    part1_count = 0
    part2_count = 0

    for policy, password in letters:
        length, letter = policy.split(" ")
        start, stop = length.split("-")
        start, stop = int(start), int(stop)

        if check_count(password, letter, start, stop):
            part1_count += 1

        if check_indexes(password, letter, start - 1, stop - 1):
            part2_count += 1

    print("Part 1", part1_count)
    print("Part 2", part2_count)