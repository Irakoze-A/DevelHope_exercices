num1 = 1122334455666

# to convert a number to string we can use str() function this is called casting

# cast num1 to string and assign to num1_str
num1_str = str(num1)

# check the length of the string
print(len(num1_str))

# get the third element of string (the one in the 3rd order)
num2 =  num1_str[2]
print(num1_str[2])

# get the 3-5 elements of string (both inclusive) by string slicing
num3 = num1_str[2:5]
print(num1_str[2:5])

# check if num2 in string (cast if necessary)
print(num2 in num1_str)   #

# check if num3 in string (cast if necessary)
print( num3 in num1_str )

# concatenate 0 to the string from left and assign to string_with_0
string_with_0 = str(0) + num1_str
print(string_with_0)

# get the characters of string_with_0 from start to position 4 (end point exclusive)
num4 = string_with_0[:4]
print(num4)

# get the characters of string_with_0 from position 5 until the end
num5 = string_with_0[5:]
print(num5)

# use negative indexing to reach the "567" string_with_0
num6 = string_with_0  # i didn't understand well. 
print(num6)