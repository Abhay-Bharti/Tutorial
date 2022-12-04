# Write a Python function to find the Max of three numbers.

print("Python function to find the Max of three numbers.")
l = []
a = int(input("No. of elements you want to add: "))
for i in range(0,a):
    s = int(input("Enter Number: "))
    l.append(s)
max = max(l)
print("Maximum number is: ",max)
print("\n")

#Write a Python function to sum all the numbers in a list.

print("Python function to sum all the numbers in a list.")
a = int(input("No. of elements you want to add: "))
l = []
for i in range(0,a):
    s = int(input("Enter Number: "))
    l.append(s)
sum = sum(l)
print("Sum of the numbers are: ",sum)
print("\n")

# Write a Python function to multiply all the numbers in a list.

print("Python function to multiply all the numbers in a list")
a = int(input("No. of elements you want to add: "))
l = []
for i in range(0,a):
    s = int(input("Enter Number: "))
    l.append(s)
product = 1
for i in l:
    product *= i
print("Product of numbers is: ",product)

#Write a Python program to reverse a string.

print("\nPython program to reverse a string.")
string = input("Enter a Word: ")
reverse = string[::-1]
print(reverse)


#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

print("\nPython function to calculate the factorial of a number")
def factorial(a):
    f = 1
    for i in range(1,a+1):
        f *= i
    print("Factorial of given number is:", f)
    return f

a = int(input("Enter Number: "))
factorial(a)

#Write a Python function that takes a list and returns a new list with unique elements of the first list.

print("\nPython function that takes a list and returns a new list with unique elements of the first list.")
def unique(L):
    U = []
    for i in L:
        if i not in U:
            U.append(i)
    print("New List with unique element:",U)

a = int(input("No. of elements you want to add: "))
L = []
for i in range(0,a):
    s = int(input("Enter Number: "))
    L.append(s)
unique(L)

# Write a Python program to print the even numbers from a given list.

print("\nPython program to print the even numbers from a given list.")
def even(l):
    u = []
    for i in l:
        if i%2 == 0:
            u.append(i)
    print("Even numbers in the given list are:",u)

a = int(input("No. of elements you want to add: "))
l = []
for i in range(0,a):
    s = int(input("Enter Number: "))
    l.append(s)
even(l)

#Print First 10 natural numbers using while loop

print("\nFirst 10 natural numbers using while loop")
def natural():
    u = []
    i = 1
    while i<11:
        u.append(i)
        i += 1
    print("Natural Numbers are: ",u)

natural()

#Write a program to print the following number pattern using a loop.

print("\nProgram to print the number pattern using a loop.")
def loop(a):
    for i in range(1, a+1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print(' ')

a = int(input("Enter any number: "))
loop(a)

#Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

print("\nProgram to accept a number from a user and calculate the sum of all numbers from 1 to a given number")
def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print(sum)

n = int(input("Enter number: "))
sum(n)

#Calculate the cube of all numbers from 1 to a given number

print("\nCalculate the cube of all numbers from 1 to a given number")
def cube(a):
    for i in range(1,a+1):
        print("Current number is:",i,"and the cube is:",i**3)

a = int(input("Enter number:"))
cube(a)

#Program to print a pattern of numbers

print("\nProgram to print a pattern of numbers ")

def pattern(num):
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print(' ')

num = int(input("Enter number: "))
pattern(num)
