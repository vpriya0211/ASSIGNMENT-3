#A Python function to sum all the numbers in a list.

def sum(numbers):
    total=0
    for i in numbers:
        total +=i
    return total
n=input("Enter the numbers: ")
num=n.split()
list=[]
for i in num:
    i=int(i)
    list.append(i)
total=sum(list)
print("Summation is: ",total)


# A Python program to reverse a string.

def reverse_string(str):
    reversed_str = ""
    for i in str:
        reversed_str = i + reversed_str
    return reversed_str
str = input("Enter a string: ")
reversed_string = reverse_string(str)
print("Reversed String:", reversed_string)

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

