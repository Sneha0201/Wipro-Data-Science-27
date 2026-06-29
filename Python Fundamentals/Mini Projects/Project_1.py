#Rides on miles

distance = int(input("How far you have to travel in miles? :"))
if distance < 3:
    print("I suggest ride a bicycle for your destination.")
elif 3 <= distance < 300:
    print("I suggest ride a motorcycle for your destination.")
else:
    print("I suggest ride a super-car for your destination.")