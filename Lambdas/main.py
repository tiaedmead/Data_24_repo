def add(num1, num2):
    return num1 + num2


print(add(4, 5))


addition = lambda num1, num2: num1 + num2


print(addition(4, 5))


savings = [234, 555, 674, 78]
bonus = list(map(lambda i: i*1.1, savings))
print(bonus)