#Write a program to print prime no. b/w 10 to 99

for i in range(10, 100):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end="\t")