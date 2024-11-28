# Problem: Write a Python program to flatten a list of lists into a single list.
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened_list = []

for sublist in list_of_lists:
    for item in sublist:
        flattened_list.append(item)

print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
