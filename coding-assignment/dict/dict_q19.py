# Problem:Write a function that returns a list of keys from a dictionary that have a specific value.

def get_keys_with_value(dict, value):
    return [k for k, v in dict.items() if v == value]

my_dict = {'a': 1, 'b': 2, 'c': 1}
print(get_keys_with_value(my_dict, 1))  # Output: ['a', 'c']
