# WAP to replace the last value of tuples in a list to 100

l = [(10,20,40), (40,50,60), (70,80,90)]

result = []

for i in l:
    result.append(i[:-1] + (100,))
print(result)