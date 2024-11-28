# Problem: Write a function that checks if a given key exists in a dictionary. If it exists, return the value, otherwise return "Key not found"

def check_key(dict, key):
    if key in dict:
        return dict[key]
    else:
        return "Key not found"

my_dict = {'a': 1, 'b': 2}
print(check_key(my_dict, 'a'))  # Output: 1
print(check_key(my_dict, 'c'))  # Output: Key not found
