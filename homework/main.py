# # Find the sum of all the multiples of 3 or 5 below 1000
#
# num = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
# print(num)
#
# # By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# # find the sum of the even-valued terms.
#
# sequence = [1, 2]
# total = 0
#
# for i in range(4000000):
#     if i == sequence[-1] + sequence[-2]:
#         sequence.append(i)
#
# for n in sequence:
#     if n % 2 == 0:
#         total += n
#
# print(total)

# # What is the largest prime factor of the number 600851475143?
#
# n = 600851475143
# i = 2
# while i * i < n:
#     while n % i == 0:
#         n /= i
#     i += 1
#
# print(n)

# # A palindromic number reads the same both ways
# # The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# # Find the largest palindrome made from the product of two 3-digit numbers
#
# max_palindrome = 0
#
# for i in range(100, 1000):
#     for j in range(100, 1000):
#         product = i * j
#         product_str = str(product)
#         if (product_str[0] == product_str[-1]) and (product_str[1] == product_str[-2]) and (product_str[2] == product_str[-3]):
#             if max_palindrome < product:
#                 max_palindrome = product
#
# print(max_palindrome)

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# def if_divides(num):
#     for i in range(2, 11):
#         if num % i != 0:
#             return False
#     else:
#         return True
#
# num = 10
# while True:
#     if if_divides(num):
#         break
#     else:
#         num += 1
#
# print(num)

# def if_divides_2(num2):
#     for i in range(2, 21):
#         if num2 % i != 0:
#             return False
#     else:
#         return True
#
# num2 = 20
# while True:
#     if if_divides_2(num2):
#         break
#     else:
#         num2 += 1
#
# print(num2)

# num = 10
# i = 2
#
# while i < 11:
#     if num % i == 0:
#         i += 1
#     else:
#         num += 1
#         i = 2
#
# print(num)
#
# num2 = 20
# i = 2
#
# while i < 21:
#     if num2 % i == 0:
#         i += 1
#     else:
#         num2 += 1
#         i = 2
#
# print(num2)

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

# sum_of_squares = sum([i * i for i in range(1, 101)])
# square_of_sum = sum(range(1, 101))
# square_of_sum = square_of_sum * square_of_sum
# print(square_of_sum - sum_of_squares)

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            return False
            break
        else:
            count += 1
    if count == n-2:
        return True

#Finds the value for the given nth term
# def term(n):
#     x = 0
#     count = 0
#     while count != n:
#         x += 1
#         if is_prime(x) == True:
#             count += 1
#     print(x)
#
#
# term(10001)

# count = 0
#
# for i in range(2,100000000):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         count += 1
#     if count == 10001:
#         print(i)
#         break

# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

one_k_digit = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
adjacent_length = 13
greatest_product = 0

for i in range(0, len(one_k_digit) - adjacent_length + 1):

    product = 1

    for j in range(i, adjacent_length + i):

        product *= int(one_k_digit[j])

    if product > greatest_product:

        greatest_product = product

print(greatest_product) #23514624000
