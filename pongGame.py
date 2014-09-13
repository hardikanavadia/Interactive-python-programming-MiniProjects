# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 650
HEIGHT = 425       
BALL_RADIUS = 30
PAD_WIDTH = 10
PAD_HEIGHT = 100
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

#ball values
ball_pos=[WIDTH/2,HEIGHT/2];
ball_vel=[random.randrange(4,6),-random.randrange(4,6)];

#pos values
p2_pos=HEIGHT/2;
p1_pos=HEIGHT/2;
p1_vel=p2_vel=0;

#scores
score1=score2=0;
# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left

def ball_init(right):
    global ball_pos
    global ball_vel
    global hits 
    ball_pos=[WIDTH/2,HEIGHT/2];
    if(right==True):
        ball_vel=[random.randrange(6,8),-random.randrange(3,7)];
    else:
        ball_vel=[-random.randrange(6,8),-random.randrange(3,7)];
      

# define event handlers
def init():
    global p1_pos, p2_pos, p1_vel, p2_vel 
    global score1, score2 
    ball=random.randrange(0,2);
    if(ball==0):
        ball_init(False);
    else:
        ball_init(True);
    #paddle values
    p2_pos=HEIGHT/2;
    p1_pos=HEIGHT/2;
    p1_vel=p2_vel=0;
    #scores
    score1=score2=0;    

def draw(game):
    global score1, score2, p1_pos, p2_pos, ball_pos, ball_vel,hits
 

    x1=p1_pos+p1_vel;
    if(x1<HALF_PAD_HEIGHT):
        x1=HALF_PAD_HEIGHT;
    elif(x1>HEIGHT-HALF_PAD_HEIGHT-1):
        x1=HEIGHT-1-HALF_PAD_HEIGHT
    x2=p2_pos+p2_vel;
    if(x2<HALF_PAD_HEIGHT):
        x2=HALF_PAD_HEIGHT;
    elif(x2>HEIGHT-HALF_PAD_HEIGHT-1):
        x2=HEIGHT-1-HALF_PAD_HEIGHT
    p1_pos=x1;
    p2_pos=x2;       
    # draw mid line and gutters
    game.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 5, "Blue")
    game.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 3, "Blue")
    game.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 3, "Blue")
    
    # draw paddles
    #paddle1
    game.draw_polygon([[0, p1_pos+HALF_PAD_HEIGHT], [PAD_WIDTH,p1_pos+HALF_PAD_HEIGHT ], [PAD_WIDTH, p1_pos-HALF_PAD_HEIGHT],[0,p1_pos-HALF_PAD_HEIGHT]], 1, "Green", "Red");
    #paddle2
    game.draw_polygon([[WIDTH-1, p2_pos+HALF_PAD_HEIGHT], [WIDTH-1-PAD_WIDTH,p2_pos+HALF_PAD_HEIGHT ], [WIDTH-1-PAD_WIDTH, p2_pos-HALF_PAD_HEIGHT],[WIDTH-1,p2_pos-HALF_PAD_HEIGHT]], 1, "Green", "Green");
    
    # update ball
    
    x1=ball_pos[0]+ball_vel[0];
    x2=ball_pos[1]+ball_vel[1];
    
    if(x2<BALL_RADIUS):
        x2=BALL_RADIUS;
        ball_vel[1]=-ball_vel[1];
    elif(x2>HEIGHT-1-BALL_RADIUS):
        x2=HEIGHT-1-BALL_RADIUS;
        ball_vel[1]=-ball_vel[1];
    if(x1<BALL_RADIUS+PAD_WIDTH):
       if(x2<p1_pos+HALF_PAD_HEIGHT and x2 > p1_pos-HALF_PAD_HEIGHT):
            x1=BALL_RADIUS+PAD_WIDTH+10;
            ball_vel[0]=-ball_vel[0];
            ball_vel[1]=ball_vel[1];
       else:
            score2=score2+1;
            ch=random.randrange(0,2);
            if(ch==0):
                ball_init(False);
            else:
                ball_init(True);
            return;    
    elif(x1> WIDTH-1-BALL_RADIUS-PAD_WIDTH) :  
        if(x2<p2_pos+HALF_PAD_HEIGHT and x2 > p2_pos-HALF_PAD_HEIGHT):
            x1=WIDTH-1-BALL_RADIUS-PAD_WIDTH-10;
            ball_vel[0]=-ball_vel[0];
            ball_vel[1]=ball_vel[1];
        else:
            score1=score1+1;
            ch=random.randrange(0,2);
            if(ch==0):
                ball_init(False);
            else:
                ball_init(True);
            return;
    
    
    ball_pos[0]=x1;
    ball_pos[1]=x2;           
    # draw ball and scores
    game.draw_circle(ball_pos,BALL_RADIUS,2,"White","Yellow"); 
    game.draw_text(str(score1),[WIDTH/4,50],50,"White");
    game.draw_text(str(score2),[WIDTH-WIDTH/4,50],50,"White");
    
def keydown(key):
    global p1_vel, p2_vel
    temp=10
    #player1
    if(key==simplegui.KEY_MAP["W"]):
        p1_vel=-temp;
    if(key==simplegui.KEY_MAP["S"]):
        p1_vel=temp;
    #player2
    if(key==simplegui.KEY_MAP["up"]):
        p2_vel=-temp;
    if(key==simplegui.KEY_MAP["down"]):
        p2_vel=temp;
    
def keyup(key):
    global p1_vel, p2_vel
    #player1
    if(key==simplegui.KEY_MAP["W"]):
        p1_vel=0;
    if(key==simplegui.KEY_MAP["S"]):
        p1_vel=0;
    #player2
    if(key==simplegui.KEY_MAP["up"]):
        p2_vel=0;
    if(key==simplegui.KEY_MAP["down"]):
        p2_vel=0;

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 200)


# start frame
init()
frame.start()
