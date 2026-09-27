import pygame as py 
py.init()
screen = py.display.set_mode((700, 700))
py.display.set_caption(("flappy bird game"))
running = True 
game_over = False
py.mixer.init()

score = 0



bird = py.image.load("flappy bird.png")
bird = py.transform.scale(bird, (50, 50))
bird_sprite = bird.get_rect()
by = 350
bird_sprite.center=(100,by)

game_over_music = py.mixer.music.load("logicallism-incorrect-buzzer-374194.mp3")

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
gravity = 0.2

vx = 1

while running:
    by = by + gravity
    pipe_sprite1.x = pipe_sprite1.x -vx
    pipe_sprite2.x = pipe_sprite2.x -vx
    pipe_sprite3.x = pipe_sprite3.x -vx
    pipe_sprite4.x = pipe_sprite4.x -vx
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
                    if event.key == py.K_SPACE:
                        for i in range(5):
                            by  = by - 5
  
    screen.fill("light blue")
    score_text = font.render("score: " + str(score), True, "black")


    if (bird_sprite.colliderect(pipe_sprite1) or
        bird_sprite.colliderect(pipe_sprite2) or
        bird_sprite.colliderect(pipe_sprite3) or
        bird_sprite.colliderect(pipe_sprite4)):
        
        game_over = True

    
    if pipe_sprite1.x < 0:
         score = score+ 1
         pipe_sprite1.x = 700
    if pipe_sprite2.x < 0:
          pipe_sprite2.x = 700
    if pipe_sprite3.x < 0:
        pipe_sprite3.x = 700
    if pipe_sprite4.x < 0:
        score = score +1
        pipe_sprite4.x = 700
         
    
    bird_sprite.center = (100, by)
    screen.blit(bird, bird_sprite)
    screen.blit(pipe, pipe_sprite1)
    screen.blit(pipe, pipe_sprite2)
    screen.blit(pipe2, pipe_sprite3)
    screen.blit(pipe2, pipe_sprite4)
    screen.blit(score_text, (300,100))

    score_text = font.render("score: " + str(score), True, "black")
    screen.blit(score_text, (300, 100))

    if game_over:
        game_over_text = font.render("GAME OVER", True, "red")
        screen.blit(game_over_text, (220, 320))
        vx = 0
        gravity = 0
        py.mixer.music.play(1)

    
    py.display.update()

py.quit()