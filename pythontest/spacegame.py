import pygame as pyg
from ship import *
from world import *
from bullet import *
import math

screen_size=[1024,512]

pyg.init()
pyg.display.set_mode(screen_size)
pyg.display.set_caption("Window")

surface=pyg.display.get_surface()

world_list=world(surface)

myship=ship(25)
myship.set_position(pyg.Vector2(screen_size[0]*0.5,screen_size[1]*0.5))

world_list.add_object(myship)

quit=False

frame_time=pyg.time.get_ticks()

W_PRESSED=False
D_PRESSED=False
A_PRESSED=False

FORWARD_ACCElERATION=100
ANGULAR_ACCELERATION=math.radians(360)

while not quit:
    for event in pyg.event.get():
        if event.type==pyg.QUIT:
            quit=True
        if event.type==pyg.KEYDOWN or event.type==pyg.KEYUP:
            if event.key==pyg.K_w:W_PRESSED=not W_PRESSED
            if event.key==pyg.K_d:D_PRESSED=not D_PRESSED
            if event.key==pyg.K_a:A_PRESSED=not A_PRESSED
            if event.key==pyg.K_SPACE:
                world_list.add_object(bullet(myship.position,myship.get_direction()))
    
    if W_PRESSED:
        myship.set_acceleration(myship.get_direction()*FORWARD_ACCElERATION)
    else:
        myship.set_acceleration(pyg.Vector2(0,0))
    if D_PRESSED:
        myship.set_angular_acceleration(ANGULAR_ACCELERATION)
    elif A_PRESSED:
        myship.set_angular_acceleration(-ANGULAR_ACCELERATION)
    else:
        myship.set_angular_acceleration(0)
        
    new_frame_time=pyg.time.get_ticks()
    world_list.update((new_frame_time-frame_time)/1000)
    frame_time=new_frame_time
    pyg.display.flip()
    surface.fill(pyg.Color(0,0,0))
pyg.quit()