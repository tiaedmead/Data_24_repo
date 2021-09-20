# # Use a backslash (\) to escape quotes
# escape_example_1 = 'I said \'WOW!\''
# print(escape_example_1)
#
# # You can also use quotes in quotes
# quotes_in_quotes_1 = 'I said "WOW!"'
# print(quotes_in_quotes_1)
# quotes_in_quotes_2 = "I said 'WOW!'"
# print(quotes_in_quotes_2)
#
# # Use the strip() function to remove spaces
# white_space = "          ~A lot of white space~          ."
# print(len(white_space))
# print(len(white_space.strip()))
# print(white_space.strip())
#
# # Use the lstrip() function to remove spaces from the left
# white_space_left_remove = "          ~A lot of white space~          ."
# print(len(white_space_left_remove))
# print(len(white_space_left_remove.lstrip()))
# print(white_space_left_remove.lstrip())
#
# # Use the lstrip() function to remove spaces from the left
# white_space_right_remove = ".          ~A lot of white space~          "
# print(len(white_space_right_remove))
# print(len(white_space_right_remove.rstrip()))
# print(white_space_right_remove.rstrip())

# F Strings
name = "lassie"
age = 7
height_cm = 60.2

print(f"{name} is {age} years old and {height_cm}cm tall")

name = "Snoopy"
years = 52

print(f"{name.upper()} is {years * 7} years old in DOG YEARS")