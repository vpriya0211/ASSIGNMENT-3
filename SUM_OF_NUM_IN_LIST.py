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
