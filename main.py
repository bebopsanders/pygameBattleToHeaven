import pygame as pg

WIDTH = 1200
HEIGHT = 600
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()

running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
    
