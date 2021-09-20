print("What is your name?")
name = input()
print("How old are you?")
age = input()
print("When is your DOB?")
dob = input()

print(f"Hello {name}, you are {age} and your date of birth is {dob}")
print(f"In dog years, your age is {int(age) * 7}")