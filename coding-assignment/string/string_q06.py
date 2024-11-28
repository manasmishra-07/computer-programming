# Problem: Write a function that counts how many times a specific character appears in a string
def count_char(s, char):
    return s.count(char)

string = "hello world"
print(count_char(string, 'o'))  # Output: 2
