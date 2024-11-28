# Problem: Write a function that checks if a substring exists within a string
def contains_substring(s, sub):
    return sub in s

string = "hello world"
substring = "world"
print(contains_substring(string, substring))  # Output: True
