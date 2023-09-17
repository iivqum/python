from world_object import world_object
import ship as shipclass
import pygame as pyg

BULLET_SIZE=5
BULLET_SPEED=200

class bullet(world_object):
    def fire(self,object):
        self.collider.set_size([15,15])
        self.set_position(object.position.copy())
        self.set_velocity(object.get_direction().copy()*BULLET_SPEED+object.velocity.copy())
        self.object=object
    def collide(self,object):
        if isinstance(object,shipclass.ship) and self.object!=object:
            self.world.delete_object(object)
    def update_object(self,dt):
        surface=self.world.surface
        size=surface.get_size()
        if self.position.x>size[0] or self.position.x<0:
            self.world.delete_object(self)
        if self.position.y>size[1] or self.position.y<0:
            self.world.delete_object(self)
    def draw(self):
        surface=self.world.surface
        rect=pyg.Rect(self.position.x-BULLET_SIZE*0.5,self.position.y-BULLET_SIZE*0.5,BULLET_SIZE,BULLET_SIZE)
        pyg.draw.rect(surface,pyg.Color(255,255,255),rect)
        pyg.gfxdraw.rectangle(surface,self.collider.rect,pyg.Color(255,0,0))