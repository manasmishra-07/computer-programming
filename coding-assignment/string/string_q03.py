# Problem:Write a function that counts the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

string = "hello world"
print(count_vowels(string))  # Output: 3
