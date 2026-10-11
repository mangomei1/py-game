
import pygame
import random
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Car Racing Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)



obstcal2_image = pygame.image.load("obstacle1.png").convert_alpha()
obstcal2_image = pygame.transform.scale(obstcal2_image, (60, 100))
obstaclsprite2 = obstcal2_image.get_rect(midtop=(400, -100))

obstacle = pygame.image.load("obstacle2.png").convert_alpha()
obstacle = pygame.transform.scale(obstacle, (60, 60))
obstaclesprite = obstacle.get_rect(midtop=(250, -100))

highway = pygame.image.load("top view of hihgway.png").convert()
highway =pygame.transform.scale(highway, (800, 800))

highway2 = pygame.image.load("top view of hihgway.png").convert()
highway2 = pygame.transform.scale(highway2, (800, 800))

car_image = pygame.image.load("car top vie.png").convert_alpha()
car_image = pygame.transform.rotate(car_image, 90)
car_image = pygame.transform.scale(car_image, (60, 100))
car = car_image.get_rect(midbottom=(400, 770))

obstcal3_image = pygame.image.load("cone.png").convert_alpha()
obstcal3_image = pygame.transform.scale(obstcal3_image, (60, 100))
obstaclsprite3 = obstcal3_image.get_rect(midtop=(600, 300))
obstaclesprite.center = (300,100)
obstaclsprite2.center = (200,400)
obstaclsprite3.center =(400,200)

speed = 3
hy1 = 0
hy2 = -800
score = 0
running = True



while running:
    hy1 += 5
    hy2 += 5


    obstaclesprite.y = obstaclesprite.y + speed
    obstaclsprite2.y = obstaclsprite2.y + speed
    obstaclsprite3.y = obstaclsprite3.y + speed
   
    if hy1 >= 800:
        hy1 = -800
    if hy2 >= 800:
        hy2 = -800

    if obstaclesprite.y >=800:
        obstaclesprite.x = random.randint(0,700)
        obstaclesprite.y = 0
    if obstaclsprite2.y >= 800:
        obstaclsprite2.x = random.randint(0,700)
        obstaclsprite2.y = 0
    if obstaclsprite3.y >=800: 
        obstaclsprite3.x = random.randint(0,700)
        obstaclsprite3.y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car.x -= speed
    if keys[pygame.K_RIGHT]:
        car.x += speed
    if keys[pygame.K_UP]:
        car.y -= speed
    if keys[pygame.K_DOWN]:
        car.y += speed

    if car.colliderect(obstaclsprite2) or car.colliderect(obstaclesprite) or car.colliderect(obstaclsprite3):
        text = font.render("Game Over! Final Score: " + str(score), True, (255, 0, 0))

        screen.blit(text, (200, 400))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    screen.blit(highway, (0, hy1))
    
    screen.blit(highway2, (0, hy2))
    screen.blit(car_image, car)
    screen.blit(obstcal2_image, obstaclsprite2)
    screen.blit(obstacle, obstaclesprite)
    screen.blit(obstcal3_image, obstaclsprite3)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
