import pygame as pyg

#basic rectangle collider class
class collider:
    def __init__(self,size,position):
        self.width=size[0]
        self.height=size[1]
        self.calculate_rect(position)
    def set_size(self,size):
        self.width=size[0]
        self.height=size[1]
    def check_collision(self,other):
        return self.rect.colliderect(other)
    def calculate_rect(self,position):
        self.rect=pyg.Rect(position.x-self.width*0.5,position.y-self.height*0.5,self.width,self.height)
    def set_position(self,p):
        self.calculate_rect(p)