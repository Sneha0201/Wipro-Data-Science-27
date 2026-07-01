# WAP to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values
dict = {"name": "gattu", "age":8, "city":"bhopal"}
print("Keys:")
for key in dict:
    print(key)
print("\nValues:")
for value in dict.values():
    print(value)
print("\nKeys and Values:")
for key, value in dict.items():
    print(key, ":", value)