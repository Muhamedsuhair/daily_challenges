import random

print("Welcome to the Guessing Game")
print("I'm thinking of a number between 1 and 100")
cguess=random.randint(1,100)
guess=int(input("Guess the number:"))
while cguess!=guess:
    if guess > cguess :
        print("guess is  high")
        guess=int(input("Guess the number:"))
    else :
        print("guess is  low")
        guess=int(input("Guess the number:"))
print("congrats you guessed correctly")        




