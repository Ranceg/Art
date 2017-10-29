import pygame as pg
import sys,time
from pygame.locals import *
pg.init()

#create a square drawing surface width = 300, height = 300

rw =50
rh = rw

DISPLAYSURF = pg.display.set_mode((300,300))
#give window a caption
pg.display.set_caption('My First Game!')

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
    r = 255
    b = 0
    v = 256
    for z in xrange(v):
    #center + dispwidth/rw   
        pg.draw.rect(DISPLAYSURF,(int(r),255,int(b)),(z+0,z+0,rw,rh))
        pg.display.update()
        time.sleep(.01)
        b += 1
        r -= 1
        z+=1
        
