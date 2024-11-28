# Problem:Given two dictionaries, update the first dictionary with the values from the second dictionary.
def update_dict(dict1, dict2):
    dict1.update(dict2)
    return dict1

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(update_dict(dict1, dict2))  # Output: {'a': 1, 'b': 3, 'c': 4}
