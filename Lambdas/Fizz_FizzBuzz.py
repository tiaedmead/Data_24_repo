# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

def fizzbuzz(i):

    if i % 15 == 0:
        return "FizzBuzz"

    elif i % 3 == 0:
        return "Fizz"

    elif i % 5 == 0:
        return "Buzz"

    else:
        return i

