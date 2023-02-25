import random
def start_playing():
    global score
    counter = 0
    print('Welcome again, we have a rundom number, between 1 and 10, try to guess the number only in 3 times')
    n = random.randint(1,10)
    guess = int(input('Enter your guess : '))
    counter += 1
    while guess != n:
        if counter == 3 :
            print('Limit Hit :(')
            break
        if guess > n:
            print('Too high')
            guess = int(input('Enter your guess : '))
        elif guess < n:
            print('Too low')
            guess = int(input('Enter your guess : '))
        counter += 1
    if guess == n:
        score += 1
        print('You have the correct number')
        
score  = 0

print("Want to play a guessing game ?")
print('Menu')
print('1 Start playing \n2.get score \n3.Exit')
select = int(input('Enter your choice:'))

while select != 3:
    if select == 1:
        start_playing()
    if select == 2 :
        print('score : ',score)
    print('Menu')
    print('1 Start playing \n2.get score \n3.Exit')
    select = int(input('Enter your choice:'))
    
if select == 3:
    print('Goodbye')