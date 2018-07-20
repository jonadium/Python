from random import randint

Number = randint(0,10)
print("Welcome to PRAPRA GUESS GAME!!!")

while True:
    Guess = int(input("Enter your guess:"))
    if Guess == Number :
        print('CONGRATULATIONS!!! Your guess was Correct')
        break
    elif Guess > Number:
        print('Guess is too high')
    elif Guess < Number:
        print('Guess too low')

print("End of GAME")
