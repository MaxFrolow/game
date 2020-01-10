import pygame
class Knight(object):
    def __init__(self):
        self.textures = []
        self.x = 179
        self.y = 179
        self.width = 50
        self.height = 60
        self.speed = 5
        self.isJump = False
        self.jump_high = 10
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.last_move = 'move_down'
        self.isInventory = False


        self.anim_count = 5

        self.strangerWalkLeft = [pygame.image.load('images/knight/knt1_lf1.gif'), pygame.image.load('images/knight/knt1_lf2.gif')]
        self.strangerWalkRight = [pygame.image.load('images/knight/knt1_rt1.gif'), pygame.image.load('images/knight/knt1_rt2.gif')]
        self.strangerWalkUp = [pygame.image.load('images/knight/knt1_bk1.gif'), pygame.image.load('images/knight/knt1_bk2.gif')]
        self.strangerWalkDown = [pygame.image.load('images/knight/knt1_fr1.gif'), pygame.image.load('images/knight/knt1_fr2.gif')]
        self.inventory_skin = pygame.image.load('images/inventory_skin.gif')





    def move(self, keys):
        if self.anim_count + 1 >= 8:
            self.anim_count = 0

        if keys[pygame.K_UP]:
            if (self.x, self.y - 5) not in self.textures \
                    and (self.x + 5, self.y - 5) not in self.textures \
                    and (self.x + 10, self.y - 5) not in self.textures \
                    and (self.x + 20, self.y - 5) not in self.textures:
                self.y -= self.speed

            self.move_up = True
            self.move_down = False
            self.position('move_up')
            self.last_move = 'move_up'
        if keys[pygame.K_DOWN]:
            if (self.x, self.y + 5) not in self.textures \
                    and (self.x + 5, self.y + 5) not in self.textures \
                    and (self.x + 10, self.y + 5) not in self.textures \
                    and (self.x + 20, self.y + 5) not in self.textures:
                self.y += self.speed
            self.move_up = False
            self.move_down = True
            self.position('move_down')
            self.last_move = 'move_down'
        if keys[pygame.K_LEFT]:
            if (self.x - 5, self.y) not in self.textures:
                self.x -= self.speed
            self.move_left = True
            self.move_right = False
            if keys[pygame.K_UP]:
                self.last_move = 'move_up'
            elif keys[pygame.K_DOWN]:
                self.last_move = 'move_down'
            else:
                self.position('move_left')
                self.last_move = 'move_left'
        if keys[pygame.K_RIGHT]:
            if (self.x + 5, self.y) not in self.textures \
                    and (self.x + 10, self.y) not in self.textures \
                    and (self.x + 20, self.y) not in self.textures \
                    and (self.x + 30, self.y) not in self.textures \
                    and (self.x + 35, self.y) not in self.textures:
                self.x += self.speed
            self.move_left = False
            self.move_right = True
            if keys[pygame.K_UP]:
                self.last_move = 'move_up'
            elif keys[pygame.K_DOWN]:
                self.last_move = 'move_down'
            else:
                self.position('move_right')
                self.last_move = 'move_right'
        self.anim_count += 1

    def append_textures(self, textures):
        self.textures += textures

    def remove_textures(self):
        self.textures = []





