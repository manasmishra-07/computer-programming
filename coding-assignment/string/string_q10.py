# Problem: Write a function that removes all occurrences of a specific character from a string.
def remove_char(s, char):
    return s.replace(char, "")

string = "hello world"
print(remove_char(string, 'o'))  # Output: "hell wrld"

