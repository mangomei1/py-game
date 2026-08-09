import pygame as py
import random
py.init()
screen = py.display.set_mode((700, 700))
py.display.set_caption("space invaders")
running = True
ship_image = py.image.load("space ship 1.png")
ship_image = py.transform.scale(ship_image, (150, 150))
ship_sprite = ship_image.get_rect()
ship_sprite.center = (50, 300)
ship_image2 = py.image.load("space ship 2.png")
ship_image2 = py.transform.scale(ship_image2, (150, 150))
ship_image2 = py.transform.rotate(ship_image2,180)
ship_sprite2 = ship_image2.get_rect()
ship_sprite2.center = (650, 300)
meteor_image = py.image.load("Meteor-drawing-11-removebg-preview.png")
meteor_image = py.transform.scale(meteor_image, (50, 50))
m1y = 50
m2y = 50
meteor_sprite = meteor_image.get_rect()
meteor_sprite.center = (650, m1y)
meteor_sprite2 = meteor_image.get_rect()
meteor_sprite2.center=(50, m2y)
while running:
    m1y = m1y +0.5
    m2y = m2y +0.5
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False


    keys = py.key.get_pressed()
    if keys[py.K_LEFT] and ship_sprite.x > 0:
        ship_sprite.x = ship_sprite.x - 5
    if keys[py.K_RIGHT] and ship_sprite.x < 300:
        ship_sprite.x = ship_sprite.x + 5
    if keys[py.K_UP] and ship_sprite.y > 0:
        ship_sprite.y = ship_sprite.y - 5
    if keys[py.K_DOWN] and ship_sprite.y < 650:
        ship_sprite.y = ship_sprite.y + 5
    if m1y > 650:
        m1y = 50
        meteor_sprite.x = random.randint(50,650)
    if m2y > 650:
        m2y = 50
        meteor_sprite2.x = random.randint(50,650)
    screen.fill(("black"))
    screen.blit(ship_image, ship_sprite)
    screen.blit(ship_image2, ship_sprite2)
    meteor_sprite.center = (50, m1y)
    meteor_sprite2.center=(650, m2y)
    screen.blit(meteor_image, meteor_sprite)
    screen.blit(meteor_image, meteor_sprite2)
    py.display.update()
   
py.quit()
