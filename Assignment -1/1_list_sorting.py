""" 
Question 1 : Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
"""

def sort_by_last_element(sampl_list):
    result = sorted(sampl_list, key=last_tuple_element)
    return result

def last_tuple_element(tupl):
    return tupl[-1]

print(format(" Example 1 ","-^30"))
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sort_by_last_element(sample_list)
print("Original List :",sample_list)
print("Sorted List:", sorted_list,"\n")

print(format("Example 2 ","-^30"))
sample_list = [(2, 7), (2, 2), (4, 3), (5, 4), (9, 5)]
sorted_list = sort_by_last_element(sample_list)
print("Original List :",sample_list)
print("Sorted List:", sorted_list)

