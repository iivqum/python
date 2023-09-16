from world_object import *
import pygame as pyg

BULLET_SIZE=5

class bullet(world_object):
    def __init__(self,position,dir):
        world_object.__init__(self)
        self.collider.set_size([15,15])
        self.set_position(position.copy())
        self.set_acceleration(dir.copy()*50)
    def draw(self,surface):
        rect=pyg.Rect(self.position.x-BULLET_SIZE*0.5,self.position.y-BULLET_SIZE*0.5,BULLET_SIZE,BULLET_SIZE)
        pyg.gfxdraw.rectangle(surface,rect,pyg.Color(255,255,255))
        pyg.gfxdraw.rectangle(surface,self.collider.rect,pyg.Color(255,0,0))