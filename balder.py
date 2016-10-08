# -*- coding: utf-8 -*-

import random
players = input("Welcome to Balderdashy2!\nPlease enter the number of players: ")

#player_count = 0
#if server response success add one



print('We will play with', players, 'players.\n')

words_fp = open('words.txt', 'r')

wordbank = []
player_def = [][]
all_def = [][]

for line in words_fp:
    wordbank.append(line.strip())



definitions_fp = open('definitions.txt', 'r')
definitions = []

for line in definitions_fp:
    definitions.append(line.strip())



#begin game
random_number = random.randint(0,len(wordbank))
print(wordbank[random_number])
actual_definition = defintions[random_number]
print(actual_definition) #just for testing
print(definitions[random_number])


for player_num in range(players): #checks
    print("Player ", player_num, "Please enter a defintion: "))
    definition = input() #add player defintion

    player_def[player_num][0].append(defintion) #I think this works add def to player list
    continue


random_order = []
#makes sure each number is unique
random_order = random.sample(range(1,players+2), players+1) #plus 2 because range

for def_number in range(players+1) #players + definition added


    all_def[def_number][]
