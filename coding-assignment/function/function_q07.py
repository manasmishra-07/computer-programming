# problem:Write a function that counts the number of vowels in a string.
def count_vowels(s):
    return sum(1 for char in s if char in 'aeiou')

print(count_vowels("hello"))  # Output: 2
