# A Python program to reverse a string.

def reverse_string(str):
    reversed_str = ""
    for i in str:
        reversed_str = i + reversed_str
    return reversed_str
str = input("Enter a string: ")
reversed_string = reverse_string(str)
print("Reversed String:", reversed_string)
