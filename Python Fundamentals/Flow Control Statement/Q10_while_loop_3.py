#WAP to check if given number is palindrome or not

n = int(input("Enter a number: "))
rev = 0
temp = n
while temp > 0:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp //= 10
if n == rev:
    print(n, "is palindrome")
else:
    print(n, "is not palindrome")