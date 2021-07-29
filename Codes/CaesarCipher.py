#!/usr/bin/env python3

print(r'''

_________                                      _________ .__       .__                  
\_   ___ \_____    ____   ___________ _______  \_   ___ \|__|_____ |  |__   ___________ 
/    \  \/\__  \ _/ __ \ /  ___/\__  \\_  __ \ /    \  \/|  \____ \|  |  \_/ __ \_  __ \
\     \____/ __ \\  ___/ \___ \  / __ \|  | \/ \     \___|  |  |_> >   Y  \  ___/|  | \/
 \______  (____  /\___  >____  >(____  /__|     \______  /__|   __/|___|  /\___  >__|   
        \/     \/     \/     \/      \/                \/   |__|        \/     \/       
  

''')



def cipher_algo(message,shift,chose):
    # alphabets to help shift the values of message
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z',
                'a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']

    if shift > 25:
        shift %= 25
    
    if chose == "E":
        cipher_text = ""
        #accessing each letter in the given message
        for char in message:
            if char in alphabet:
                # getting the index of individual letter
                position = alphabet.index(char)
                # adding shift value and defining new shift position
                new_pos = position + shift
                # accessing shifted position and assigning that as a new letter
                new_letter = alphabet[new_pos]
                # adding new letter to the empty string
                cipher_text += new_letter
            else:
                cipher_text += char

        print(f"Your encoded messege is: {cipher_text}")
        
    elif chose == "D":
        plain_text = ""
        # same logic as above just substracting the shift value
        for char in message:
            if char in alphabet:
                position = alphabet.index(char)
                new_pos = position - shift
                new_letter = alphabet[new_pos]
                plain_text += new_letter
            else:
                plain_text += char

        print(f"Your decoded messege is: {plain_text}")

    elif chose == "Q":
        print("Good Bye")
        quit()

       




if __name__ == '__main__':

    while True:
        text = input("Enter your message -> ").lower()
        shift_value = int(input("Enter shift value -> "))
        # choise of user
        ch = input("Chose what you want \
            \n E. for encode \n D for decode\n Q for quit -->  ").upper()

        cipher_algo(text,shift_value,ch)

