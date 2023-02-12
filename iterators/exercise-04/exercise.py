list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for i in list1 :
    print(i)
 
for i in tuple1:
    print(i)
    
for id,val in enumerate(set1):
    print(val)
    
for key, element in dict1.items():
    if element =='land':
        print(f"{key} lives in {element}")