# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 04:14:59 2016

@author: noahgirard
"""
import random
players = input("Welcome to Balderdashy2!\nPlease enter the number of players: ")

print('We will play with', players, 'players.\n')

words_fp = open('words.txt', 'r')

wordbank = []

for line in words_fp:
    wordbank.append(line.strip())
    


definitions_fp = open('definitions.txt', 'r')
definitions = []

for line in definitions_fp:
    definitions.append(line.strip())
    


#begin game
random_number = random.randint(0,len(wordbank))
print(wordbank[random_number])
print(definitions[random_number])