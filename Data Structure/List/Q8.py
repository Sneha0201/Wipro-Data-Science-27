# WAP to remove the first occurence of a specified element from a list

list = [10,20,30,40,30,20]
val = 30
if val in list:
    list.remove(val)
    print("Updated list:", list)
else:
    print("Value not found in list")