# Problem: Write a Python program to remove all occurrences of a given element from a list.
my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = 2

while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # Output: [1, 3, 4, 5]
