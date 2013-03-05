# implementation of card game - Memory
# Angel Inokon 

# CodeSkulptor http://www.codeskulptor.org/#user5-DLJ6MKtKIk-4.py
import simplegui
import random

# Global Variables and Constants
CARD_WIDTH = 50
CARD_HEIGHT = 100
NUM_CARDS = 16
CANVAS_WIDTH = CARD_WIDTH * NUM_CARDS
CANVAS_HEIGHT = 100
CARD_RANGE = 8
FONT_SIZE = 24
MARGIN = CARD_WIDTH/4
num_turns = 0

# helper function to initialize globals

def create_cards():
    global cards
    cards =[]
    for i in range(CARD_RANGE):
        cards.append(i)
        cards.append(i)
    pass

def if_paired():
    return cards[first_mate_index] == cards[second_mate_index]

def rect_coords(i):
    a = (i+1)*CARD_WIDTH
    b = 0
    c = i*CARD_WIDTH
    d = CARD_HEIGHT
    card_pos = [(a, b), (a, d), (c, d), (c, b)]
    return card_pos


# Ooops. I didn't see random.shuffle() in the instructions. 
# Well I learned something...Ha ha!
#def shuffle_deck():
#    global cards
#    value = 0
#    remaining_cards = list(cards)
#    for i in range(len(cards)):
#        value = random.randrange(0,len(remaining_cards))
#        cards[i] = remaining_cards[value]
#        remaining_cards.remove(cards[i])
#    pass

def init():
    global cards, exposed_list, state, first_mate_index, second_mate_index, num_turns
    create_cards()
    random.shuffle(cards)
    exposed_list = []
    state = 0
    first_mate_index = 0
    second_mate_index = 0
    num_turns = 0
    for i in range(NUM_CARDS):
       exposed_list.append(0)
    print cards
    pass  

     
# define event handlers
def mouseclick(pos):
    global state, first_mate_index, second_mate_index, num_turns
    i = pos[0]//50 
    if (exposed_list[i] == 0):
        if state == 0 or state ==1:
           num_turns +=1
           if not if_paired():
                exposed_list[first_mate_index] = 0
                exposed_list[second_mate_index] = 0
           first_mate_index = i
           exposed_list[first_mate_index] = 1
           state = 2
        elif state == 2:
           second_mate_index = i
           exposed_list[second_mate_index] = 1
           state = 1
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    '''Draw the cards on the stage using a for statement'''
    for i in range(len(cards)):
        if exposed_list[i]:
          canvas.draw_text(str(cards[i]), (CARD_WIDTH*i+MARGIN, CANVAS_HEIGHT//2+MARGIN), FONT_SIZE, "White")
        else:
          canvas.draw_polygon(rect_coords(i), 1, "Black", "Green")
        pass
    '''Update the label'''
    l.set_text("Moves: "+str(num_turns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.add_button("Restart", init)
l=frame.add_label("Moves: 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()