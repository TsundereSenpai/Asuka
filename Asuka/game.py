#importing
import random
import pygame
import os
import time
import math
from config import *


#define terms
width = 1200
height = 900
FPS = 60

#define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bgc = (30,18,36)
sbc = (30,30,30)


#folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")




#SFX
pygame.init()
hitSound = pygame.mixer.Sound("Pew.wav")
pygame.mixer.music.load("bee.mp3")
font_name = pygame.font.match_font('arial')



def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,5))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        hurtboxCenter = self.rect.center
    def update(self):
        speed = 5
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LSHIFT]:
                speed = 2
        else:
                speed = 5
        if keystate[pygame.K_LEFT]:
                self.rect.x -= speed
        if keystate[pygame.K_RIGHT]:
                self.rect.x += speed
        if keystate[pygame.K_UP]:
                self.rect.y -= speed
        if keystate[pygame.K_DOWN]:
                self.rect.y += speed
        if self.rect.right > width-417.5:
                self.rect.right = width-417.5
        if self.rect.left < 17.5:
                self.rect.left = 17.5
        if self.rect.top < 32.5:
                self.rect.top = 32.5
        if self.rect.bottom > height-32.5:
                self.rect.bottom = height-32.5


        
    

class Hurtbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"Reimu6.gif")).convert()
        self.image.set_colorkey(bgc)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        hurtboxCenter = self.rect.center
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LSHIFT]:
                speed = 2
        else:
                speed = 5
        if keystate[pygame.K_LEFT]:
                self.rect.x -= speed
        if keystate[pygame.K_RIGHT]:
                self.rect.x += speed
        if keystate[pygame.K_UP]:
                self.rect.y -= speed
        if keystate[pygame.K_DOWN]:
                self.rect.y += speed
        if self.rect.right > width-400:
                self.rect.right = width-400
        if self.rect.left < 0:
                self.rect.left = 0
        if self.rect.top < 0:
                self.rect.top = 0
        if self.rect.bottom > height:
                self.rect.bottom = height
        
        


class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join(img_folder,"wasp.png")).convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(width- 400 - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 6)
        def update(self):
            self.rect.y += self.speedy
            if self.rect.top > height + 10:
                self.rect.x = random.randrange(width - 400 - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, enemyMaxSpeed)


"""
class SB(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((400,900))
            self.image.fill(sbc)
            self.rect = self.image.get_rect()
            self.rect.x = 800
            self.rect.y = 0
"""
class Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Bird.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 400

class Mori(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "mori.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = 875
        self.rect.y = 750


#Title Screen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("東方蜂の森")
clock = pygame.time.Clock()

bg = pygame.image.load(os.path.join(img_folder, "bg.jpg")).convert()
bg_rect = bg.get_rect()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
hurtbox = Hurtbox()
player = Player()
logo = Logo()
mori = Mori()
#sb = SB()
all_sprites.add(hurtbox)
all_sprites.add(player)
#all_sprites.add(sb)
all_sprites.add(logo)
all_sprites.add(mori)
for i in range(enemyAmount):
	m = Mob()
	all_sprites.add(m)
	mobs.add(m)
	
#Start game
running = True
IFr = 100
score = 0
constantScore = math.ceil((enemyMaxSpeed * enemyAmount) / (initLife * 20))
pygame.mixer.music.play(-1)
while Life > 0:
       
        
        screen.blit(bg,(0,0))
        #FPS
        clock.tick(FPS)
        #events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        IFr = IFr + 1
        
        print(IFr)
        #updates
        all_sprites.update()
        #Pew

        
        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits and IFr > 100:
            Life = Life - 1
            pygame.mixer.Sound.play(hitSound)
            print("Pew pew")
            IFr = 0
            Player().rect.x = 400
            Player().rect.y = 450
            
            
            
        if IFr >= 100:
            screen.fill(sbc)
            screen.blit(bg, bg_rect)
            score = score + constantScore

        if IFr < 100:
            screen.fill(black)


        draw_text(screen, "Total Score", 24, 1000, 10)
        draw_text(screen, str(score), 18, 1000, 50)
        draw_text(screen, "Remaining Life", 24, 1000, 150)
        draw_text(screen, str(Life), 18, 1000, 190)
            
                
        #Drawing
        
        
        all_sprites.draw(screen)
        #flips
        pygame.display.flip()
        if running == False:
            pygame.quit()
pygame.mixer.music.stop()
time.sleep(5)
pygame.quit()
