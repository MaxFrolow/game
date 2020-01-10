import sys, pygame
from source.character.stranger import Knight
from source.locations.tavern import *

pygame.init()

win = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Quest')




class Stranger(Knight):
    def position(self, move):
        anim_count = self.anim_count // 4
        if move == 'move_up':
            #pygame.draw.rect(win, (255, 255, 255), (stranger.x, stranger.y, 1, 1))
            win.blit(self.strangerWalkUp[anim_count], (self.x - self.width/2, (self.y - self.height)))
        elif move == 'move_down':
            #pygame.draw.rect(win, (255, 255, 255), (stranger.x, stranger.y, 1, 1))
            win.blit(self.strangerWalkDown[anim_count], (self.x - self.width/2 , (self.y - self.height)))
        elif move == 'move_left':
            #pygame.draw.rect(win, (255, 255, 255), (stranger.x, stranger.y, 1, 1))
            win.blit(self.strangerWalkLeft[anim_count], (self.x - self.width/2, (self.y - self.height)))
        elif move == 'move_right':
            #pygame.draw.rect(win, (255, 255, 255), (stranger.x, stranger.y, 1, 1))
            win.blit(self.strangerWalkRight[anim_count], (self.x - self.width/2,  (self.y - self.height)))

    def inventory(self, show, view):

        #check is inventory are open and if open - show
        if show == True:
            if self.isInventory:
                win.blit(stranger.inventory_skin, (200, 100))
        #wait of event opening ore closing inventory
        if view == True:
            if self.isInventory == True:
                self.isInventory = False
            elif self.isInventory == False:
                self.isInventory = True

def render(hero, location):
    hero.append_textures(location.textures)




run = True

stranger = Stranger()
tavern = Tavern()
render(stranger, tavern)
while run:
    pygame.time.delay(70)
    win.blit(tavern.back_ground, (0, 0))
    for i in range(len(tavern.textures)):
        pygame.draw.rect(win, (0,0,0), (tavern.textures[i][0], tavern.textures[i][1] ,1,1))



    if stranger.isInventory:
        stranger.inventory(show=True, view=False)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            stranger.inventory(show=False, view=True)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        stranger.move(keys)
        print(stranger.x, stranger.y)
    else:
        stranger.position(stranger.last_move)




    if keys[pygame.K_ESCAPE]:
        run = False



    pygame.display.update()



pygame.quit()