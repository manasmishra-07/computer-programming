# Problem: Write a Python program to remove all duplicate elements from a list.
my_list = [1, 2, 3, 2, 4, 5, 3]
unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)  # Output: [1, 2, 3, 4, 5]
