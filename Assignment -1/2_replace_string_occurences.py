"""
Question 2: Write a Python program to get a string from a given string where all occurrences of its first char have been
changed to "$", except the first char itself. 
Sample String :'restart';
"""

def replace_char(strng):
    if not strng :
        return ""
    first_char = strng[0]
    remaining_string = strng[1:]
    return first_char+remaining_string.replace(first_char,"$")

string_1 = "restart"
string_2 = "Python Programming Plus"

print(format(" Example 1 ","-^30"))
print("Original String :",string_1)
print("Replaced String :",replace_char(string_1),"\n")
print(format(" Example 2 ","-^30"))
print("Original String :",string_2)
print("Replaced String :",replace_char(string_2),"\n")