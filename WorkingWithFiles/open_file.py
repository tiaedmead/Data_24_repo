file = open("order.txt")

file_content = file.readlines()

for line in file_content:
    print(line.replace("\n", ""))

file.close()

# A different way to write the above
# with open("order.txt") as file:
#
#     file_content = file.readlines()
#
#     for line in file_content:
#         print(line.replace("\n", ""))

with open("order.txt", "w") as file:

    order_items = ["wings", "pizza", "juice"]

    for item in order_items:
        file.write(item + "\n")