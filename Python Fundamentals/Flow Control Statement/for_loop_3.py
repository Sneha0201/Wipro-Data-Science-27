#Write a program to check if given no. is prime or not.

n = int(input("Enter a number: "))
if n <= 1:
    print(n, "is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not prime")
            break
    else:
        print(n, "is Prime")