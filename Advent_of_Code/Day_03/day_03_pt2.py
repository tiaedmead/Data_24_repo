# tree_count = 0
# right = 1
# down = 1
# x = 0
# y = 0
#
# with open("input.txt") as file:
#     lines = file.read().splitlines()
#
#     while y < len(lines):
#         line = lines[y]
#
#         for n in range(1, 6):
#             line = line + line
#
#         if line[x] == "#":
#             tree_count += 1
#
#         x = x + int(right)
#         y = y + int(down)
#
#     print(f"trees on slope (1, 1) is {tree_count}")
#
# tree_count = 0
# right = 3
# down = 1
# x = 0
# y = 0
#
# with open("input.txt") as file:
#     lines = file.read().splitlines()
#
#     while y < len(lines):
#         line = lines[y]
#
#         for n in range(1, 6):
#             line = line + line
#
#         if line[x] == "#":
#             tree_count += 1
#
#         x = x + int(right)
#         y = y + int(down)
#
#     print(f"trees on slope (3, 1) is {tree_count}")
#
# tree_count = 0
# right = 5
# down = 1
# x = 0
# y = 0
#
# with open("input.txt") as file:
#     lines = file.read().splitlines()
#
#     while y < len(lines):
#         line = lines[y]
#
#         for n in range(1, 21):
#             line = line + line
#
#         if line[x] == "#":
#             tree_count += 1
#
#         x = x + int(right)
#         y = y + int(down)
#
#     print(f"trees on slope (5, 1) is {tree_count}")
#
# tree_count = 0
# right = 7
# down = 1
# x = 0
# y = 0
#
# with open("input.txt") as file:
#     lines = file.read().splitlines()
#
#     while y < len(lines):
#         line = lines[y]
#
#         for n in range(1, 21):
#             line = line + line
#
#         if line[x] == "#":
#             tree_count += 1
#
#         x = x + int(right)
#         y = y + int(down)
#
#     print(f"trees on slope (7, 1) is {tree_count}")
#
# tree_count = 0
# right = 1
# down = 2
# x = 0
# y = 0
#
# with open("input.txt") as file:
#     lines = file.read().splitlines()
#
#     while y < len(lines):
#         line = lines[y]
#
#         for n in range(1, 6):
#             line = line + line
#
#         if line[x] == "#":
#             tree_count += 1
#
#         x = x + int(right)
#         y = y + int(down)
#
#     print(f"trees on slope (1, 2) is {tree_count}")
#
#
total =  67 * 211 * 77 * 89 * 37
print(total)