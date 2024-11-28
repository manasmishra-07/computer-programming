# Problem:Write a function that returns the sum of the digits of a number.
def sum_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_digits(123))  # Output: 6
