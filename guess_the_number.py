#submitted By: hardik anavadia
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


# initialize global variables used in your code
counter = 7
active_game = ''
comp_number = 0

# helper function to start and restart the game
def new_game():
    print "new game"
    print "number of remaining guess is 7"
       
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global comp_number
    global counter
    global active_game
    active_game = 1
    comp_number = random.randrange(0, 101)
    counter = 7
    print " "
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is ", counter


def range1000():
    # button that changes range to range [0,1000) and restarts
    global comp_number
    global counter
    global active_game
    active_game = 0
    secret_number = random.randrange(0, 1001)
    counter = 7
    print " "
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is ", counter
    
def input_guess(guess):
        if guess.isdigit():
            guess = int(guess)
            print "your guess was:", guess
        else:
            print "Please enter a valid input..."
            print ""
    
    
    # main game logic goes here	
        global active_game
        global counter
        global comp_number
        
        counter = counter - 1
        print "Number of remaining guesses is ", counter
        
        if(comp_number > guess):
            print("Guess higher!")
            print ""

        elif(comp_number < guess):
            print("Guess lower!")
            print ""
        else:
            print("congrats...! your guess is successful")
            if active_game:
                range100()
            else:
                range1000()
        if counter <= 0:
            print "You have lost."
            if active_game:
                range100()
            else:
                range1000()




# create frame

f = simplegui.create_frame("guess the number", 300, 300)

f.add_button("range is [0,100)", range100, 200)
f.add_button("range is [0,1000)", range1000, 200)
f.add_input("enter your guess", input_guess, 200)

# register event handlers for control elements



# call new_game and start frame
range100()
f.start()


# always remember to check your completed program against the grading rubric
