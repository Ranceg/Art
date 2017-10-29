import pygame as pg
import sys,time
from pygame.locals import *
pg.init()

#create a square drawing surface width = 300, height = 300
dispwidth = 500
rw = 75
rh = rw
dispheight = dispwidth/2
DISPLAYSURF = pg.display.set_mode((dispwidth,dispheight))
#give window a caption
pg.display.set_caption('Gradient swipe!')

#loop forever
while True:
    #get user events
    for event in pg.event.get():
        if event.type == QUIT:
            #end game and close window
            pg.quit()
            sys.exit()
    #otherwise update display
    #rect. draw parameters{
    #Display to draw on,
    #show a rectangle(no red, fully green, no blue),
    #at pos on screen(from top left(xright,ydown) and rect size (w,h)
   
    xcenter = dispwidth / 2 - rw/2
    ycenter = dispheight / 2 - rh/2
    quart = dispwidth / 4
    c = 150
    r = 255
    g = 0
    b = 0
    d = dispwidth/2


    
    
    for i in xrange(d+quart-150):
        
        
        pg.draw.rect(DISPLAYSURF,(int(r),int(g),int(b)),(i + xcenter - quart,ycenter,rw,rh))
        b += 1
        r -= 1
        i += 1
        time.sleep(.0101)
        pg.display.update()
        for j in xrange(d-quart-150):
        
        
            pg.draw.rect(DISPLAYSURF,(int(r),int(g),int(b)),(j + xcenter - quart,ycenter,rw,rh))
            b += 1
            g += 1
            r -= 1
            time.sleep(.01)
            j += 2
            pg.display.update()

