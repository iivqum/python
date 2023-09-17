from world_object import *
import pygame as pyg

BULLET_SIZE=5
BULLET_SPEED=200

class bullet(world_object):
    def fire(self,position,dir):
        self.collider.set_size([15,15])
        self.set_position(position.copy())
        self.set_velocity(dir.copy()*BULLET_SPEED)
    def draw(self,surface):
        rect=pyg.Rect(self.position.x-BULLET_SIZE*0.5,self.position.y-BULLET_SIZE*0.5,BULLET_SIZE,BULLET_SIZE)
        pyg.draw.rect(surface,pyg.Color(255,255,255),rect)
        pyg.gfxdraw.rectangle(surface,self.collider.rect,pyg.Color(255,0,0))