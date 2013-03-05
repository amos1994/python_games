# Implementation of classic arcade game Pong
# Angel Inokon
# 11/16/12 - Submission

Codeskulptor link http://www.codeskulptor.org/#user8-fpCye2Uwx7-8.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# helper function that spawns a ball, returns a position vector and a velocity vector
def random_spawn_direction():
    return random.randrange(0,2)

def random_velocity():
    global ball_vel
    ball_vel[0] = random.randrange(120, 240)//60
    ball_vel[1] = random.randrange(60, 180)//60

def going_right():
    return ball_pos[0]>WIDTH/2


def check_paddle_collision():
    ball_collided = 0
    
    if not going_right() and (ball_pos[1]-BALL_RADIUS <= paddle1_pos + HALF_PAD_HEIGHT) and (ball_pos[1]+BALL_RADIUS >= paddle1_pos - HALF_PAD_HEIGHT):
            ball_collided = 1
    elif going_right() and (ball_pos[1]-BALL_RADIUS <= paddle2_pos + HALF_PAD_HEIGHT) and (ball_pos[1]+BALL_RADIUS >= paddle2_pos - HALF_PAD_HEIGHT):
            ball_collided = 1
    return ball_collided

 
    
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT/2]
    ball_vel = [1,1]
    random_velocity()
    if not right:
      ball_vel[0]= -ball_vel[0]
    pass

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(random_spawn_direction())
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    pass

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_vel > 0:
        if (paddle1_pos+HALF_PAD_HEIGHT+paddle1_vel <= HEIGHT):
            paddle1_pos += paddle1_vel
    if  paddle1_vel < 0: 
        if (paddle1_pos-HALF_PAD_HEIGHT+paddle1_vel >= 0):
            paddle1_pos += paddle1_vel

    if paddle2_vel > 0:
        if (paddle2_pos+HALF_PAD_HEIGHT+paddle2_vel <= HEIGHT):
            paddle2_pos += paddle2_vel
    if  paddle2_vel < 0: 
        if (paddle2_pos-HALF_PAD_HEIGHT+paddle2_vel >= 0):
            paddle2_pos += paddle2_vel
            
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles  
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT],
        [HALF_PAD_WIDTH, paddle1_pos+HALF_PAD_HEIGHT], PAD_WIDTH,
        "White")
    c.draw_line([WIDTH-HALF_PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT],
        [WIDTH-HALF_PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT], 
        PAD_WIDTH, "White")
     
    # update ball
    '''Check if it hit top or bottom wall'''
    if ball_pos[1] <= BALL_RADIUS:
       ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
       ball_vel[1] = - ball_vel[1]
    
    '''Check if it hit the left or right gutter'''
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH: # CHECK LEFT GUTTER
        if check_paddle_collision():
           ball_vel[0] = - ball_vel[0]*1.1
        else: 
            score2 += 1
            ball_init(1)
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS: #CHECK RIGHT GUTTER
        if check_paddle_collision():
           ball_vel[0] = - ball_vel[0]*1.1
        else: 
            score1 +=1
            ball_init(0)
    
    ''' Update the position of the ball. Animates at 60 frames per second'''
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

            
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1), (WIDTH/4,50), 24, "White")
    c.draw_text(str(score2), (WIDTH/4+WIDTH/2,50), 24, "White")
    
    
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 4
    
    

    
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel=0
    paddle2_vel=0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()

