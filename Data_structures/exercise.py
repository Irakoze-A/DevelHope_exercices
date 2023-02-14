list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

print(len(list1))
print(len(tuple1))
print(len(set1))
print(len(dict1))

print(list1[0])
print(tuple1[0])
print(dict1['lion'])

list1[1] = "rabbit"
# tuple1[1] = "rabbit"  # tuple is ummutable, couldn't be changed
list1.append("monkey")
list1.remove("rabbit")

dict1['fish'] = 0