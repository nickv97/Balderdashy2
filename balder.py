# -*- coding: utf-8 -*-
#oh lol neither of these things work.
#I wonder if we can actually get it to work.

import random
while True:
    try:
        players = int(input("Welcome to Balderdashy2!\nPlease enter the number of players: "))
        break
    except (ValueError, TypeError):
        print("Oops! that was no valid number. Try again...")


#player_count = 0
#if server response success add one

def get_key(item): #for sorting the list
    return item[0] #first element sorting - the number


def random_list(item):


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
    print("Player ", player_num, "Please enter a defintion: ")
    definition = input() #add player defintion

    player_def[player_num].append(defintion) #I think this works add def to player list
    player_def[player_num][]
    continue


random_order = []
#makes sure each number is unique
random_order.append(random.sample(range(1,players+2), players+1)) #plus 2 because range

for def_number in range(players+1) #players + definition added

    player_def
    all_def[def_number][]


#sort items now
