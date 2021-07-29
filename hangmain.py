#!/usr/bin/env python3
import random


print(r'''
  ___ ___                                              
 /   |   \_____    ____    ____   _____ _____    ____  
/    ~    \__  \  /    \  / ___\ /     \\__  \  /    \ 
\    Y    // __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \
 \___|_  /(____  /___|  /\___  /|__|_|  (____  /___|  /
       \/      \/     \//_____/       \/     \/     \/ 
       ''')

def hangman():
    word_list = ["ardvark","baboon","camel","apple","insert", "your", "words", "inside", "this", "python", "list",'tree', 'mango', 'coding', 'human', 'python', 'java','hangman', 'amazon', 'help', 'football', 'cricket', 'direction', 'dress', 'apology', 'driver', 'ship', 'pilot']


    # randomly chosen word from word_list
    chosen_word = random.choice(word_list)

    # for programmer's check
    # print(f"the solution is {chosen_word}")

    # create blanks
    display = []
    for _ in chosen_word:
        display += "_"
    print(display)


    lives = 6
    end = False
    while not end:

        # taking user guess
        guess = input("Guess a letter: ").lower()
        # checking guess in the chosen_word

        if guess in display:
            print(f"You've already guessed {guess}")

        for pos in range(len(chosen_word)):
            letter = chosen_word[pos]
            if letter == guess:
                display[pos] = letter
        
        if guess not in chosen_word:
            lives -= 1
            print(f"Wrong guess, current lives: {lives}")
            if lives == 3:
                hint = input("Take a hint, you'll lose 2 lives. Y(yes),N(no): ").upper()
                if hint == "Y":
                    lives -= 2
                    print(f"The last two words are:\n{' '.join(chosen_word[len(chosen_word)-2])} , {' '.join(chosen_word[len(chosen_word)-1])}\n")
                elif hint == "N":
                    continue
            elif lives == 0:
                end = True
                print("You lose")
        
        #printing current word from user's guess
        print(f"Current word is: {' '.join(display)}")
        

        if "_" not in display:
            print("You won")
            end = True

if __name__ == '__main__':
    hangman()