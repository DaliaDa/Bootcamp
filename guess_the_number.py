import random

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = input("guess a number between 1 and 100: ")
    guess = int(guess)


    if guess == number:
        print("Yup, You won!")
        break
    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")
