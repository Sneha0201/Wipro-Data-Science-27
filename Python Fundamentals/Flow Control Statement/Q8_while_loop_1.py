#Write a program to the sum of all digits of a given no.

n = int(input("Enter a no.: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print(sum)