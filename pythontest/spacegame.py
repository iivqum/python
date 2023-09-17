import pygame as pyg
from ship import *
from world import *
from bullet import *
from ship_controller import *
import math

screen_size=[1024,512]

pyg.init()
pyg.display.set_mode(screen_size)
pyg.display.set_caption("Window")

surface=pyg.display.get_surface()

game_world=world(surface)

player_ship=ship(game_world)
player_ship.set_size(15)
player_ship.set_position(pyg.Vector2(screen_size[0]*0.5,screen_size[1]*0.5))
player_ship_controller=ship_controller(player_ship)

enemy_ship=ship(game_world)
enemy_ship.set_size(15)
enemy_ship.set_position(pyg.Vector2(screen_size[0]*0.2,screen_size[1]*0.5))
enemy_ship_controller=ship_controller(enemy_ship)

def kill_player():
    


quit=False

frame_time=pyg.time.get_ticks()

while not quit:
    for event in pyg.event.get():
        if event.type==pyg.QUIT:
            quit=True
        if event.type==pyg.KEYDOWN:
            if event.key==pyg.K_SPACE:player_ship_controller.add_action("shoot")
    keys=pyg.key.get_pressed()
    if keys[pyg.K_w]:player_ship_controller.add_action("move_forward")
    if keys[pyg.K_d]:player_ship_controller.add_action("turn_right")
    if keys[pyg.K_a]:player_ship_controller.add_action("turn_left")
            
    kill_player()      
            
    player_ship_controller.update()
    enemy_ship_controller.update()
    
    new_frame_time=pyg.time.get_ticks()
    game_world.update((new_frame_time-frame_time)/1000)
    frame_time=new_frame_time
    pyg.display.flip()
    surface.fill(pyg.Color(0,0,0))
pyg.quit()