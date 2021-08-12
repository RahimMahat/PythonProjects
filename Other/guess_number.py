'''Here we have created two projects that are diffrentiated with two different functions
 the first one is we guess the number and computer tell us is that correct or not
 and the second one is computer guess the number and we tell the number is correct high or low
 for that we imported random and randint from it two get any random number from the given range'''

import random

def guess(x):
    random_num = random.randint(1,x)  #randint basically fetch the random number in between the range you've provided
    guess = 0 #her we are initializing the while loop form 0
    while guess != random_num:
        guess = int(input(f"Guess a number from 1 to {x} : "))
        if guess < random_num:
            print("Oops, Guess again the number is low ")
        elif guess > random_num:
            print("Oops, Guess again the number is high ")

    print(f"Yay Congrats. You've guessed the right number {random_num}")

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could also be high because they both are same to check that we used this extra if else statement
        feedback = input (f"{guess} is to High(H), too Low (L), or Correct (C)? : ").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1

    print(f"Yay, the computer guessed your number correctly, the number is {guess}")


comp_guess(100)
#guess(10)

