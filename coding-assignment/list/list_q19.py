# Problem: Write a Python program to find common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = []

for item in list1:
    if item in list2:
        common_elements.append(item)

print(common_elements)  # Output: [4, 5]
