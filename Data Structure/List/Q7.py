# WAP to remove the item from a specified index in a list

list = [10,15,20,25,30]
i = 1
if 0 <= i <= len(list):
    remove_item = list.pop(i)
    print("Removed Value:", remove_item)
    print("Updated list:", list)
else:
    print("Enter valid index")