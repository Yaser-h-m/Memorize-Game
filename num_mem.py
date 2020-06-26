# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

# cg5222719036_ncdr password

import simplegui 
import random

A=16
CARD_WIDTH=50

state=0
prev1=0
prev2=0
turn=0
cards_list=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
cards_exposed=[True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

def new_game():
    global state,turn
    state=0
    turn=0
    
    random.shuffle(cards_list)
    print(cards_list)
    
    temp=0
    while temp<16:
        cards_exposed[temp]=False
        temp+=1
        

# Handler for mouse click
def mouseclick(pos):
    global state,prev1,prev2,turn
    current=0
    if state==0:
        current=pos[0]/50
        cards_exposed[current]=True
        state=1
        prev1=current
    elif state==1:
        current=pos[0]/50
        if cards_exposed[current]==False:
            cards_exposed[current]=True
            state=2
            prev2=current
    else:
        current=pos[0]/50
        turn+=1
        if cards_exposed[current]==False:
            if cards_list[prev1]!=cards_list[prev2]:
                cards_exposed[prev1]=False
                cards_exposed[prev2]=False
            cards_exposed[current]=True
            state=1
            prev1=current

# Handler to draw on canvas
def draw(canvas):
    label.set_text('Turns = '+str(turn))
    temp=0
    while temp<16:
        if cards_exposed[temp]:
            canvas.draw_text(str(cards_list[temp]),[temp*CARD_WIDTH+5,78],80,"White")
        else:
            canvas.draw_polygon([(temp*CARD_WIDTH,0),(temp*CARD_WIDTH,100),((temp+1)*CARD_WIDTH,100),((temp+1)*CARD_WIDTH,0)],1,"Brown","Green")
        temp+=1
     
        
# Create a frame and add buttons
frame = simplegui.create_frame("Memory", 800, 100)
button = frame.add_button('Restart',new_game)
label = frame.add_label('Turns = '+str(turn))

#register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# Start frame
new_game()
frame.start()