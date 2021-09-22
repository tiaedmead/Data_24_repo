def add_to_2020(n, n2):

    if n + n2 == 2020:
        return True

    else:
        return False


full_list = []

with open("input.txt", "r") as file:

    data = file.readlines()

    for i in data:
        full_list.append(int(i.replace("\n", "")))

    for i in full_list:
        for j in full_list:
            if add_to_2020(i, j):
                print(i * j )