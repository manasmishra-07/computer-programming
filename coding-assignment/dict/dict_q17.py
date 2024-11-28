# Problem:Write a function that removes all keys with a specified value from a dictionary.
def remove_key_by_value(dict, value):
    return {k: v for k, v in dict.items() if v != value}

my_dict = {'a': 1, 'b': 2, 'c': 1}
print(remove_key_by_value(my_dict, 1))  # Output: {'b': 2}
