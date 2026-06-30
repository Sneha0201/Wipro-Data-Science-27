#Check if two non-negative number have same last digit.

num1 = int(input("Enter first no.: "))
num2 = int(input("Enter second no.: "))

if num1 % 10 == num2 % 10:
    print("True")
else:
    print("False")