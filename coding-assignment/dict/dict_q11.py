# Problem: Given two dictionaries dict1 and dict2, merge them into a new dictionary. If a key is present in both dictionaries, sum their values.

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Create a copy of dict1
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 4}
