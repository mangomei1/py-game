import pygame as py
import random
import time
py.init()
screen = py.display.set_mode((700, 700))
py.display.set_caption("space invaders")
running = True
ship_image = py.image.load("space ship 1.png")
ship_image = py.transform.scale(ship_image, (100, 100))
ship_sprite = ship_image.get_rect()
ship_sprite.center = (50, 300)
ship_image2 = py.image.load("space ship 2.png")
ship_image2 = py.transform.scale(ship_image2, (100, 100))
ship_image2 = py.transform.rotate(ship_image2,180)
ship_sprite2 = ship_image2.get_rect()
ship_sprite2.center = (650, 300)
meteor_image = py.image.load("Meteor-drawing-11-removebg-preview.png")
meteor_image = py.transform.scale(meteor_image, (50, 50))
bullet_image = py.image.load("cropped bullet.png")
bullet_image = py.transform.scale(bullet_image, (15, 30))
bullet_image1 = py.transform.rotate(bullet_image, -90)
bullet_image2 = py.transform.rotate(bullet_image, 90)
bv1 = ship_sprite.x
bv2 = ship_sprite2.x
bullet_sprite = bullet_image1.get_rect()
bullet_sprite2 = bullet_image2.get_rect()
bullet_sprite.center = (bv1, ship_sprite.y)
bullet_sprite2.center = (bv2, ship_sprite2.y)

m1y = 50
m2y = 50
m1x = random.randint(50,650)
m2x = random.randint(50,650)
meteor_sprite = meteor_image.get_rect()
meteor_sprite.center = (m1x, m1y)
meteor_sprite2 = meteor_image.get_rect()
meteor_sprite2.center=(m2x, m2y)
v1 = 0
v2=0
font = py.font.Font(None, 36)
player1_score = 0
player2_score = 0

shoot1 = False
shoot2 = False

while running:
    m1y = m1y + 0.2
    m2y = m2y +0.2
    bv1 = bv1 +v1
    bv2 = bv2 +v2
    if v1 == 0:
        bullet_sprite.center = (ship_sprite.x +50, ship_sprite.y+50)
    if v2 == 0:
        bullet_sprite2.center = (ship_sprite2.x +50, ship_sprite2.y+50)

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
    if keys[py.K_a] and ship_sprite2.x > 300:
        ship_sprite2.x = ship_sprite2.x - 5
    if keys[py.K_d] and ship_sprite2.x < 650:
        ship_sprite2.x = ship_sprite2.x + 5
    if keys[py.K_w] and ship_sprite2.y > 0:
        ship_sprite2.y = ship_sprite2.y - 5
    if keys[py.K_s] and ship_sprite2.y < 650:
        ship_sprite2.y = ship_sprite2.y + 5
    if keys[py.K_SPACE]:
        shoot2 = False
        v1 = 0.5
    if keys[py.K_q]:
        shoot1 = False
        v2 = -0.5

    if m1y > 650:
        m1y = 50
        m1x = random.randint(50,650)
    if m2y > 650:
        m2y = 50
        m2x= random.randint(50,650)
    if bv1 > 650:
        bv1 = ship_sprite.x +50
        v1 = 0 
    if bv2 < 0:
        bv2 = ship_sprite2.x +50
        v2 = 0
    if bullet_sprite.colliderect(bullet_sprite2):
        shoot1 = True
        shoot2=True
        v1= 0 
        v2= 0
        bullet_sprite.center = (ship_sprite.x +50, ship_sprite.y+50)
        bullet_sprite2.center = (ship_sprite2.x +50, ship_sprite2.y+50)

    if ship_sprite.colliderect(bullet_sprite2) and shoot1 == False:
        shoot1 = True
        bullet_sprite2.center = (ship_sprite2.x +50, ship_sprite2.y+50)
        player2_score = player2_score +1
        score2_text = font.render("Player 2 Score: " + str(player2_score), True, "white")


    if ship_sprite2.colliderect(bullet_sprite) and shoot2 == False:
        shoot2 = True
        bullet_sprite.center = (ship_sprite.x +50, ship_sprite.y+50)
        player1_score = player1_score +1
        score1_text = font.render("Player 1 Score: " + str(player1_score), True, "white")

    screen.fill(("black"))
    score1_text = font.render("Player 1 Score: " + str(player1_score), True, "white")
    score2_text = font.render("Player 2 Score: " + str(player2_score), True, "white")

    screen.blit(score1_text, (20, 5))
    screen.blit(score2_text, (450, 5))
    screen.blit(ship_image, ship_sprite)
    screen.blit(ship_image2, ship_sprite2)
    meteor_sprite.center = (m1x, m1y)
    meteor_sprite2.center=(m2x, m2y)
    screen.blit(meteor_image, meteor_sprite)
    screen.blit(meteor_image, meteor_sprite2)
    screen.blit(bullet_image1, bullet_sprite)
    screen.blit(bullet_image2, bullet_sprite2)
    bullet_sprite.center = (bv1, ship_sprite.y+50)
    bullet_sprite2.center = (bv2, ship_sprite2.y+50)
    py.display.update()
   
py.quit()
