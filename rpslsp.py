#submitted By: hardik anavadia
#mini project-2
#Rock-paper-scissors-lizard-spock program

import random

#numbers and corresponding strings are assigned as bellow

# 0 - rock
# 1 - spock
# 2 - paper
# 3 - lizard
# 4 - scissors

#difining the functions

def name_to_number(name):
    if(name == 'rock'):
        result = 0
    elif(name == 'Spock'):
        result = 1
    elif(name == 'paper'):
        result = 2
    elif(name == 'lizard'):
        result = 3
    elif(name == 'scissors'):
        result = 4
    return result   

def number_to_name(number):
    if(number == 0):
        result = 'rock'
    elif(number == 1):
        result = 'Spock'
    elif(number == 2):
        result = 'paper'
    elif(number == 3):
        result = 'lizard'
    elif(number == 4):
        result = 'scissors'
    return result 

def rpsls(guess):
    
    player_number = name_to_number(guess)
    comp_number = random.randrange(0, 5)
    
    difference = (player_number - comp_number) % 5
    
    print "Player chooses", number_to_name (player_number)
    print "Computer chooses", number_to_name (comp_number)
    
    if difference == 0:
        print "Player and Computer tie!"
        print ""    
    elif difference == 1:
        print "Player Wins!"
        print ""    
    elif difference == 2:
        print "Player Wins!"
        print ""    
    elif difference == 3:
        print "Computer Wins!"
        print ""    
    else:
        print "Computer Wins!"
        print ""    
    return ""

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
