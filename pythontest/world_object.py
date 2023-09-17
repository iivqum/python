import pygame as pyg
import math
from collider import collider

class world_object:
    def __init__(self,world):
        self.position=pyg.Vector2(0,0)
        self.velocity=pyg.Vector2(0,0)
        self.acceleration=pyg.Vector2(0,0)
        self.rotation=0
        self.angular_velocity=0
        self.angular_acceleration=0
        self.collider=collider([0,0],self.position)
        
        world.add_object(self)
        self.world=world
    def update(self,dt):
        self.velocity+=self.acceleration*dt
        self.position+=self.velocity*dt
        self.angular_velocity+=self.angular_acceleration*dt
        self.rotation+=self.angular_velocity*dt
        self.collider.set_position(self.position)
        self.check_collisions
        self.update_override(dt)
    def collide(self,object):pass    
    def draw(self,surface):pass
    def check_collisions(self,objects):
        for obj in objects:
            if obj==self:continue
            if not self.collider.check_collision(obj.collider):continue
            self.collide(obj)
    def get_direction(self):
        return pyg.Vector2(math.cos(self.rotation),math.sin(self.rotation))
    def update_override(self,dt):pass
    def draw(self):pass
    def set_acceleration(self,a):
        self.acceleration=a
    def set_velocity(self,v):
        self.velocity=v
    def set_position(self,p):
        self.collider.set_position(p)
        self.position=p
    def set_angular_acceleration(self,aa):
        self.angular_acceleration=aa
    def set_angular_velocity(self,av):
        self.angular_velocity=av