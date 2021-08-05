#!/usr/bin/env python3
import pandas as pd

nato_words = pd.read_csv("nato_phonetic_alphabet.csv")
df = pd.DataFrame(nato_words)
# using dictionary comprehension on pandas dataframe
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(nato_dict)
word = input("Enter a word: ").upper()
# taking the input word and then getting the value of the letter from above dict
nato_phonetic_alphabet = [nato_dict[letter] for letter in word]
print(nato_phonetic_alphabet)
