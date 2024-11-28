# Problem:Given a nested dictionary, write a function that accesses a specific value inside the nested structure (e.g., dict['key1']['key2']).
def access_nested_dict(dict, key1, key2):
    return dict.get(key1, {}).get(key2, 'Key not found')

nested_dict = {'a': {'b': 1}, 'c': {'d': 2}}
print(access_nested_dict(nested_dict, 'a', 'b'))  # Output: 1
print(access_nested_dict(nested_dict, 'a', 'c'))  # Output: Key not found
