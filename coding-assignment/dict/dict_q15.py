# Problem:Given a dictionary, write a function that returns the key with the largest value.

def largest_value(dict):
    return max(dict, key=dict.get)

my_dict = {'a': 1, 'b': 3, 'c': 2}
print(largest_value(my_dict))  # Output: 'b'
