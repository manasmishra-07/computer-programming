# Problem:  Write a Python program to merge two lists alternately.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
merged_list = []

for i in range(len(list1)):
    merged_list.append(list1[i])
    merged_list.append(list2[i])

print(merged_list)  # Output: [1, 'a', 2, 'b', 3, 'c']
