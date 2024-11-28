# Problem: Write a Python program to find the index of the first occurrence of a specified element in a list.
my_list = [10, 20, 30, 40, 50]
element = 30

index = -1
for i in range(len(my_list)):
    if my_list[i] == element:
        index = i
        break

print(f"Index of {element}: {index}")  # Output: Index of 30: 2
