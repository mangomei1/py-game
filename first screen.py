import pygame as py
import random
py.init()
screen = py.display.set_mode((700, 700))
py.display.set_caption("green screen")
running = True 
bird_image = py.image.load("bird-removebg-preview.png")
bird_image = py.transform.scale(bird_image, (200,200))
bird_sprite =bird_image.get_rect()
bird_sprite.center = (350, 350)
insect_image = py.image.load("ladybug-removebg-preview.png")
insect_image =py.transform.scale(insect_image,(50,50))
insect_sprite = insect_image.get_rect()
insect_sprite.center=(100,100)
bird_image2 = py.image.load("bird 2.png")
bird_image2 = py.transform.scale(bird_image2, (100,100))
bird_sprite2 = bird_image2.get_rect()
bird_sprite2.center = (250, 250)
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False 

    keys = py.key.get_pressed()
    if keys[py.K_a]:
        bird_sprite.x -= 5
    if keys[py.K_d]:
        bird_sprite.x += 5
    if keys[py.K_w]:
        bird_sprite.y -= 5
    if keys[py.K_s]:
        bird_sprite.y += 5
    if keys[py.K_LEFT]:
        bird_sprite2.x -= 5
    if keys[py.K_RIGHT]:
        bird_sprite2.x += 5
    if keys[py.K_UP]:
        bird_sprite2.y -= 5
    if keys[py.K_DOWN]:
        bird_sprite2.y += 5
    if bird_sprite.colliderect(insect_sprite):
        insect_sprite.x = random.randint(50,650)
        insect_sprite.y = random.randint(50,650)
    screen.fill(("green"))
    screen.blit(bird_image, bird_sprite)
    screen.blit(insect_image, insect_sprite)
    screen.blit(bird_image2, bird_sprite2)
    py.display.update()
py.quit()