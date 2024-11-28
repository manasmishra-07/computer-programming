# Problem:Given a list, create a dictionary that counts the frequency of each item.
def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict

my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
print(count_occurrences(my_list))  # Output: {'apple': 2, 'banana': 3, 'orange': 1}
