import pygame
import math

FORWARD_ACCELERATION=100
ANGULAR_ACCELERATION=math.radians(360)

class ship_controller:
    def __init__(self,ship):
        self.ship=ship
        self.actions=dict()
    def add_action(self,key):
        self.actions.update({key:True})
    def update(self):
        self.ship.set_acceleration(pygame.Vector2(0,0))
        self.ship.set_angular_acceleration(0)
        if "move_forward" in self.actions:
            self.ship.set_acceleration(self.ship.get_direction().copy()*FORWARD_ACCELERATION)
        if "turn_left" in self.actions:
            self.ship.set_angular_acceleration(-ANGULAR_ACCELERATION)
        if "turn_right" in self.actions:
            self.ship.set_angular_acceleration(ANGULAR_ACCELERATION)
        if "shoot" in self.actions:
            self.ship.fire_bullet()
        self.actions.clear()        
    