# Problem:Write a function that counts how many times a specific value appears in a list.
def count_occurrences(lst, val):
    return lst.count(val)

print(count_occurrences([1, 2, 3, 2, 2], 2))  # Output: 3
