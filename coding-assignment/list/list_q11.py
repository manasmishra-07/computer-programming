# Problem: Write a Python program to find both the maximum and minimum element in a list.
my_list = [4, 2, 8, 5, 1, 7]
max_element = my_list[0]
min_element = my_list[0]

for num in my_list:
    if num > max_element:
        max_element = num
    if num < min_element:
        min_element = num

print(f"Maximum: {max_element}, Minimum: {min_element}")
