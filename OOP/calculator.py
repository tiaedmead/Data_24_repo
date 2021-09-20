def addition(*multiargs: int) -> int:
    result =  sum(multiargs)
    print(result)

def addition2(*multiargs: int) -> int:
    result =  0
    for arg in multiargs:
        result += arg
    return result

def subtraction(num1: int, num2: int) -> int:
    result = num1 - num2
    print(result)

def division(num1: int, num2: int) -> int:
    result = num1 / num2
    print(result)

def multiplication(num1: int, num2: int) -> int:
    result = num1 * num2
    print(result)

print("Please select an operation:")
print("1 for addition")
print("2 for subtraction")
print("3 for division")
print("4 for multiplication")
