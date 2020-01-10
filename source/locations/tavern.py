import pygame

class Texture(object):
    def __init__(self):
        self.place = []
        self.left_x = 200
        self.high_y = 200
        self.len_x = 50
        self.len_y = 50
        self.back_ground = pygame.image.load('images/chair.png')

        for x in range(self.left_x, (self.left_x + self.len_x)):
            for y in range(self.high_y, (self.high_y + self.len_y)):
                self.place.append((x, y))

class Location(object):
    def __init__(self):
        self.back_ground = pygame.image.load('images/tavern.png')
        self.npc = []
        self.textures_obj=[]
        self.textures=[]

    def x_line_texture(self, line):
        for x in range(601):
            for y in range(line, (line + 5)):
                self.textures.append((x, y))

    def y_line_texture(self, line):
        for y in range(401):
            for x in range(line, line + 5):
                self.textures.append((x, y))

    def append_obj(self, obj):
        if type(obj) == list or type(obj) == tuple:
            self.textures_obj += obj
            for x in obj:
                self.textures += x.place
        else:
            self.textures_obj.append(obj)
            self.textures += obj.place





class Tavern(Location):
    def __init__(self):
        super().__init__()
        self.hero_init_x = (210)
        self.hero_init_y = (210)
        self.high_line = 171
        table = Texture()
        self.x_line_texture(self.high_line)
        self.x_line_texture(400)
        self.y_line_texture(0)
        self.y_line_texture(600)
        self.append_obj(table)



