# This program tells you to fuck off and wants your name to forge your identity... And then you can guess a number chosen by the "CPU"
import random

guessesTaken = 0

print ("Fuck you!")
print ("Give me your fucking name so I can steal your identity")
myName = input()

number = random.randint(1, 20)
print ("Alright, I'll enjoy your identity!" ", Oh and guess a number from 1 - 20, " + myName)

for guessesTaken in range (6):
    print("Fecking Guess Something!") #Four spaces in front of "print"
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Jekus, your guess is too low, I'm afraid") # Eight spaces in front of "print"

    if guess > number:
        print("Jekus you guessed too high I'm afraid...")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("Jekus that was a good guess, " + myName + "! You guessed in " +
          guessesTaken + " guesses!")

if guess != number:
    number = str(number)
    print("Jekus, you fecking suck, it was fecking, " + number + ".")
    
#Updated to stop crash on normal launch#
print("Press Enter to exit...")
input()  # or input("...") if you want a prompt message
