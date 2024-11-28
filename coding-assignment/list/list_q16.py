# Problem: Write a Python program to check if a list is sorted in ascending order.
my_list = [1, 2, 3, 4, 5]
is_sorted = True

for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
        is_sorted = False
        break

print(f"Is the list sorted? {is_sorted}")  # Output: True
