#Create a list of 5 integers and display list items. Access individual elements from index

list = [10,20,30,40,50]
print("List items:")
for item in list:
    print(item)
for i in range(len(list)):
    print(f"Element at list {i}: {list[i]}")