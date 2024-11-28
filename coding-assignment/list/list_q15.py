# Problem: Write a Python program to find the sum of all even numbers in a list.
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
sum_even = 0

for num in my_list:
    if num % 2 == 0:
        sum_even += num

print(f"Sum of even numbers: {sum_even}")  # Output: Sum of even numbers: 20
