# Problem: Write a Python program to find the second largest element in a list.
my_list = [10, 20, 4, 45, 99]
first_largest = second_largest = float('-inf')

for num in my_list:
    if num > first_largest:
        second_largest = first_largest
        first_largest = num
    elif num > second_largest and num != first_largest:
        second_largest = num

print(f"Second largest element: {second_largest}")  # Output: 45
