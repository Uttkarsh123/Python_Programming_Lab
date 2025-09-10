""" Question 3 : Write a Python program to find the first appearance of the  substring'not' and 'poor' from a given string.
If 'bad' follows the 'poor', replace the whole 'not'....'poor' substring with 'good'.
Return the resulting string."""

def replace_poor_not(text):
    index_not = text.find("not")
    index_poor = text.find("poor")
    
    #Checking if poor comes after not
    if index_not !=-1 and index_poor !=-1 and index_not<index_poor:
        new_text = text[:index_not]+"good"+text[index_poor+len("poor"):]
        return new_text

    return text
    
    
original_text_1 = "The Food is not that poor"
replaced_text_1 = replace_poor_not(original_text_1)
print(format(" Example _1 ","*^30"))
print("Original String :",original_text_1)
print("String After replacement :",replaced_text_1,"\n")

original_text_1 = "The lyrics are not that poor"
replaced_text_1 = replace_poor_not(original_text_1)
print(format(" Example _2 ","*^30"))
print("Original String :",original_text_1)
print("String After replacement :",replaced_text_1)