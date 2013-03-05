# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(number): 
    # convert number to a name using if/elif/else  
    if number == 0:
       name = "rock"
    elif number == 1:
       name = "Spock"  
    elif number == 2:
       name = "paper"
    elif  number == 3:
       name = "lizard"
    else: 	
        name ="scissors"
    return name
    
def name_to_number(name):
    # fill in your code below
    # convert name to number using if/elif/else
    
    if name == "rock":
        number = 0
    elif name == "Spock":
        number =1
    elif name == "paper":
        number =2
    elif name == "lizard":
        number =3
    else: 	
        number =4
    return number

def rpsls(guess): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(guess)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # compute difference of player_number and comp_number modulo five
    winner_calc = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if winner_calc == 1:
        winner = "Player"
    elif winner_calc == 2:
        winner = "Player"
    elif winner_calc == 3:
        winner = "Computer"
    elif winner_calc == 4:
        winner = "Computer"
    else: 
        winner ="Tie"
    # convert comp_number to name using number_to_name
    name = number_to_name(comp_number)
    
    # print results
    print "Player chooses " + guess
    print "Computer chooses " + name
    if winner == "Tie":
        print "Player and Computer tie!"
    else:
        print winner + " wins!"
    print ""
    
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


