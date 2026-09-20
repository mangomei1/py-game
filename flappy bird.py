import pygame as py 
py.init()
screen = py.display.set_mode((700, 700))
py.display.set_caption(("flappy bird game"))
running = True 


score = 0

bird = py.image.load("flappy bird.png")
bird = py.transform.scale(bird, (50, 50))
bird_sprite = bird.get_rect()
bird_sprite.center=(100,350)

pipe = py.image.load("pipe.png")
pipe = py.transform.scale(pipe, (70,350))

pipe_sprite1 = pipe.get_rect()
pipe_sprite1.center=(200,650)

pipe_sprite2 = pipe.get_rect()
pipe_sprite2.center=(500,550)

pipe2= py.transform.rotate(pipe, 180)
pipe_sprite3 = pipe2.get_rect()
pipe_sprite3.center = (200,150)

pipe_sprite4 = pipe2.get_rect()
pipe_sprite4.center = (500,50)

font = py.font.Font(None, 36)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.fill("light blue")

    score_text = font.render("score: " + str(score), True, "black")

    screen.blit(bird, bird_sprite)
    screen.blit(pipe, pipe_sprite1)
    screen.blit(pipe, pipe_sprite2)
    screen.blit(pipe2, pipe_sprite3)
    screen.blit(pipe2, pipe_sprite4)
    screen.blit(score_text, (300,100))

    
    py.display.update()

py.quit()