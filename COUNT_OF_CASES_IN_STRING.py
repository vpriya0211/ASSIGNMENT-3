# A Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def count(str):
    upper_count = 0
    lower_count = 0
    for i in str:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    return upper_count, lower_count
str = input("Enter a string: ")
upper, lower = count(str)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
