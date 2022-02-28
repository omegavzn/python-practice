# Given a string, extend the string to a base value then find the number of occurances of a character/value within new string

# String containing characters (that form a pattern)
s = ["a","b","e","m"]

# Base number of characters in new string
n = 10

# Find the length of the string "s"
length_s = len(s)
# print(length_s) will return 4

# Find the quotient and remainder of base number divided by/modulo string length
divide_times = n // length_s
extra = n % length_s

# Define new list and add number of extra elements based on values stored within "extra" variable
new_list = divide_times * s
new_list += s[0:extra]
# print(new_list) will return list with 10 characters

# Count the number of "a" character occurances within new string
count_a = new_list.count("a")

# Number of "a" characters will return 3
print(count_a)