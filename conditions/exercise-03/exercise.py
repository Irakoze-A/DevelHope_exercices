import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

if number1 > number2 :
    print( f'number1 :{number1} is the bigger than number2 : {number2}')
elif number1< number2 :
    print(f'number1 : {number1} is smaller than number2: {number2}')
else :
    print('{number1} is equal to {number2}')
