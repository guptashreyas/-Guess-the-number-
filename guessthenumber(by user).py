import random
num = random.randint(1, 100)
guess = 0
while guess != num:
    guess = int(input("Enter an integer from 1 to 100: "))
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    else:
        print("You guessed it!")
        break
