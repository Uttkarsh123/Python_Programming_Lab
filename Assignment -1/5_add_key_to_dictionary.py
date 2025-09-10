"""
Question :5 Write a python program to add key to a dictionary.
"""

dictionary_1 = {
    "name": "Amit",
    "age":24
}
print ("Initial Dictionary :", dictionary_1) 

#new Keys
new_key_1 = "City"
new_value_1 = "New York"

new_key_2 = "Job"
new_value_2 = "Software Engineer"

#Adding Keys to Dictionary
dictionary_1[new_key_1] = new_value_1
dictionary_1[new_key_2] = new_value_2

print("Dictionary after adding new keys : ",dictionary_1)