""" 
Question 4 : Write a python program to sort a dictionary by value.
"""

def sort_dictionary_by_value(dictionary):
    result = sorted(dictionary.items(), key =get_value)
    return result

def get_value(item):
    return item[1]

print(format(" Example 1 ","*^30"))
my_dict_1 = {"apple":9,"banana":8,"mango":10,"guava":6,"kiwi":9}
sorted_dict_1= sort_dictionary_by_value(my_dict_1)
print("Original Dictionary :",my_dict_1)
print("Sorted Dictionary :",sorted_dict_1,"\n")

print(format(" Example 2 ","*^30"))
my_dict_2 = {"math": 85, "science": 90, "history": 78, "english": 92, "art": 80}
sorted_dict_2 = sort_dictionary_by_value(my_dict_2)
print("Original Dictionary :", my_dict_2)
print("Sorted Dictionary :", sorted_dict_2, "\n")