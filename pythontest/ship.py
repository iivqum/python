from world_object import *
import pygame as pyg
import pygame.gfxdraw
import math

class ship(world_object):
    def __init__(self,size):
        world_object.__init__(self)
        self.collider.set_size([size*2,size*2])
        self.size=size
    def update_override(self,dt):
       pass
    def draw(self,surface):
        p1=self.position+pyg.Vector2(math.cos(math.radians(0)+self.rotation)*self.size,math.sin(math.radians(0)+self.rotation)*self.size)
        p2=self.position+pyg.Vector2(math.cos(math.radians(120)+self.rotation)*self.size,math.sin(math.radians(120)+self.rotation)*self.size)
        p3=self.position
        p4=self.position+pyg.Vector2(math.cos(math.radians(240)+self.rotation)*self.size,math.sin(math.radians(240)+self.rotation)*self.size)  
        pyg.draw.polygon(surface,pyg.Color(255,255,255),[p1,p2,p3,p4])
        pyg.gfxdraw.rectangle(surface,self.collider.rect,pyg.Color(255,0,0))