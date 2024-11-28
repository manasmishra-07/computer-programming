# Problem:Write a function that checks if a given string is a palindrome (reads the same backward and forward).
def is_palindrome(s):
    return s == s[::-1]

string = "madam"
print(is_palindrome(string))  # Output: True
