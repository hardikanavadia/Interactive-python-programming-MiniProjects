#submitted By: hardik anavadia

#cousera | interactive python programming | mini project | stopwatch Game

import simplegui

# define global variables
global count
global min
global sec
global x, y
count = 0
sec = 0
min = 0
x = 0
y = 0
start = 0
stop = 0

# counting tenths of seconds into formatted string A:BC.D
def format(t):
    global count, sec, min
    t = count
    if (t == 10):
        sec = sec + 1
        count = 0
        
    if (sec == 60):
        min = min + 1
        sec = 0
        
# define event handlers for buttons
def start_timer():
    global start, stop
    if ((start-stop) == 0):
        start = start + 1
        timer.start()

def stop_timer():
    global x, y, start, stop
    if ((start-stop) == 1):
        stop = stop + 1
        timer.stop()
        y = y + 1
        if (count == 0):
            x = x + 1
    
def reset_timer():
    global count, sec, min, x, y
    timer.stop()
    count = 0
    sec = 0
    min = 0
    x = 0
    y = 0

def exit_timer():
    frame.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count = count + 1
    
def draw_handler(canvas):
    global count, sec, min, x, y
    format(count)
    if (sec < 10):
        canvas.draw_text(str(min)+":"+str(0)+str(sec)+"."+str(count),(80,160),60,"White")
    else:
        canvas.draw_text(str(min)+":"+str(sec)+"."+str(count),(80,160),60,"White")
    canvas.draw_text(str(x)+"/"+str(y), (10,40), 20, "Red")

# create frame
frame = simplegui.create_frame("Stopwatch:The Game",300,300)

# register event handlers
timer = simplegui.create_timer(130,timer_handler)
frame.add_button("Start",start_timer,200)
frame.add_button("Stop",stop_timer,200)
frame.add_button("Reset",reset_timer,200)
frame.set_draw_handler(draw_handler)
frame.add_button("Exit",exit_timer,200)

# start timer and frame
frame.start()
