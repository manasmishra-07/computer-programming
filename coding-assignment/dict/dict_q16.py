# Problem:Use dictionary comprehension to create a dictionary from a list of tuples where the first item in each tuple is the key and the second item is the value

def list_to_dict(lst):
    return {key: value for key, value in lst}

my_list = [('a', 1), ('b', 2), ('c', 3)]
print(list_to_dict(my_list))  # Output: {'a': 1, 'b': 2, 'c': 3}
