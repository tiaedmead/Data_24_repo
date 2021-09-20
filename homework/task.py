user_prompt = True

while user_prompt:
    age = input("How old are you? ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("You seem to be too old.  Please answer again using only numbers")