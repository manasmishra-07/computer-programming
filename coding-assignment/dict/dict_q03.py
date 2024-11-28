# Problem: You need to merge multiple dictionaries into one, with the values from later dictionaries overwriting earlier ones.

dict1 = {'name': 'Steve', 'age': 40}
dict2 = {'age': 45, 'city': 'London'}
dict1.update(dict2)
print(dict1)  