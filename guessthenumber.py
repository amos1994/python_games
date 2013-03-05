# "Guess the number" mini-project
# Angel Inokon
# 10.26.12

# input will come from buttons and an input field
# all output for the game will be printed in the console


# initialize global variables used in your code

import math
import random
import simplegui

secret_number = 0
user_guess = 0
low = 0
high = 100
num_tries = 0

# define helper functions

def generate_secret_number(low, high):
    '''Generate a random number given a range'''
    global secret_number
    secret_number = random.randrange(low,high)
    #print secret_number
    
def generate_number_of_tries(high):
    '''Find the log base 2 to calculate the number of tries given a number'''
    global num_tries
    num_tries = math.ceil(math.log(high)/math.log(2))
    print "You have", num_tries, "tries.\n"

def print_answer():
    '''Prints guesses and starts game if won'''
    global num_tries
    if user_guess < secret_number:
        print "Your guess was " + str(user_guess) + ". The secret number is higher."
        num_tries = num_tries - 1
        print "Remaining guesses: ", num_tries,"\n"
    elif user_guess > secret_number:
        print "Your guess was " + str(user_guess) + ". The secret number is lower."
        num_tries = num_tries - 1
        print "Remaining guesses: ", num_tries,"\n"
    else:
        print "Your guess was " + str(user_guess) + ". The secret number is " + str(secret_number) + ". You win!"
        start_game()

        
def start_game():
    '''Keeps the current range and calls the range function'''
    if high == 1000:
       range1000()
    else:
       range100()
                
# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100] and restarts
    global low
    global high
    low = 0
    high = 100
    generate_secret_number(low,high)
    print "\n*** New Game ***\nThe range is from 0 to 100."
    generate_number_of_tries(high)

def range1000():
    # button that changes range to range [0,1000] and restarts
    global low
    global high
    low = 0
    high = 1000
    generate_secret_number(low,high)
    print "\n*** New Game ***\nThe range is from 0 to 1000"
    generate_number_of_tries(1000)


def get_input(guess):
    # main game logic goes here	
    global user_guess
    global num_tries
    
    user_guess = int(guess)
    if num_tries == 0:
       print "You are out of tries. You lose. Restarting game..."
       start_game()
    else:
       print_answer()
    
# create frame
frame = simplegui.create_frame("Guess the Number", 300,300, 150)


# register event handlers for control elements
frame.add_input("Enter your guess:", get_input, 50)
frame.add_button("Range 0 to 100", range100, 150)
frame.add_button("Range 0 to 1000", range1000, 150)

# start frame
frame.start()
start_game()


