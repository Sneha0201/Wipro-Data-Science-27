# WAP to find the index of an element in a tuple

t = (10,20,30,40,50,60)
n = int(input("Enter element:"))
if n in t:
    print("Index:", t.index(n))
else:
    print("Element not found")