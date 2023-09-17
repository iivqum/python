class world:
    def __init__(self,surface):
        self.surface=surface
        self.objects=list()
    def add_object(self,object):
        self.objects.append(object)
    def update(self,dt):
        for obj in self.objects:
            obj.update(dt)
            obj.draw(self.surface)
            