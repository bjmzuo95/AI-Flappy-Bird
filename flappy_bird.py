import pygame
import neat

WIN_WIDTH = 500
WIN_HEIGHT = 800

BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load('./imgs/bird1.png')),
    pygame.transform.scale2x(pygame.image.load('./imgs/bird2.png')),
    pygame.transform.scale2x(pygame.image.load('./imgs/bird3.png')), 
]
PIPE_IMS = pygame.transform.scale2x(pygame.image.load('./imgs/pipe.png'))
BASE_IMS = pygame.transform.scale2x(pygame.image.load('./imgs/base.png'))
BG_IMS = pygame.transform.scale2x(pygame.image.load('./imgs/bg.png'))

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
        
    def move(self):
        self.tick_count += 1
        dis = self.vel * self.tick_count + 1.5 * self.tick_count ** 2
        
        if dis >= 16:
            dis = 16
        elif dis < 0:
            dis -= 2
            
        self.y = self.y + dis
        
        if dis < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else: 
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
