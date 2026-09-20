import pygame as py
import time
py.init()
running = True
screen = py.display.set_mode((700, 700))
py.display.set_caption("recycle game")
running = True
py.mixer.init()

green_bin = py.image.load("greenbin.png")
red_bin = py.image.load("red bin.png")
green_bin = py.transform.scale(green_bin, (100, 100))
red_bin = py.transform.scale(red_bin, (100, 100))
green_bin_sprite = green_bin.get_rect()
red_bin_sprite = red_bin.get_rect()
green_bin_sprite.center = (50, 600)
red_bin_sprite.center = (650,600)


paper_bag = py.image.load("paper bag.png")
newspaper = py.image.load("newspaper.png")
paper_bag = py.transform.scale(paper_bag, (50, 50))
newspaper = py.transform.scale(newspaper, (50, 50))
paper_bag_sprite = paper_bag.get_rect()
newspaper_sprite = newspaper.get_rect()
paper_bag_sprite.center = (50,100)
newspaper_sprite.center = (150,100)


bottle = py.image.load("bottle.png")
foil = py.image.load("foil.png")
bottle = py.transform.scale(bottle, (50, 50))
foil = py.transform.scale(foil, (50, 50))
bottle_sprite = bottle.get_rect()
foil_sprite = foil.get_rect()
bottle_sprite.center = (250,100)
foil_sprite.center = (350,100)

battery = py.image.load("battery.png")
battery = py.transform.scale(battery, (50, 50))
battery_sprite = battery.get_rect()
battery_sprite.center = (450,100)

banana = py.image.load("banana.png")
banana = py.transform.scale(banana, (50, 50))
banana_sprite = banana.get_rect()
banana_sprite.center = (550,100)

dragging_banana = False 
dragging_battery = False
dragging_foil = False
dragging_bottle = False
dragging_newspaper = False 
dragging_paper_bag = False

score = 0 
count = 0

font = py.font.Font(None, 36)
winner_text = ""
winner_text = font.render("" , True , "green")
incorrect_text = ""
incorrect_text = font.render("" , True , "red")
    
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.MOUSEBUTTONDOWN:
            if banana_sprite.collidepoint(event.pos):
                dragging_banana = True
            if battery_sprite.collidepoint(event.pos):
                dragging_battery = True
            if foil_sprite.collidepoint(event.pos):
                dragging_foil = True
            if bottle_sprite.collidepoint(event.pos):
                dragging_bottle = True
            if newspaper_sprite.collidepoint(event.pos):
                dragging_newspaper = True
            if paper_bag_sprite.collidepoint(event.pos):
                dragging_paper_bag = True
            
        if event.type == py.MOUSEMOTION:
            if dragging_banana == True:
                banana_sprite.center = event.pos
            if dragging_battery == True:
                battery_sprite.center = event.pos 
            if dragging_foil == True:
                foil_sprite.center = event.pos
            if dragging_bottle == True:
                bottle_sprite.center =event.pos
            if dragging_paper_bag == True:
                paper_bag_sprite.center = event.pos
            if dragging_newspaper == True:
                newspaper_sprite.center = event.pos 
        

        if event.type == py.MOUSEBUTTONUP:
            dragging_banana = False 
            dragging_battery = False
            dragging_foil = False
            dragging_bottle = False
            dragging_paper_bag = False 
            dragging_newspaper = False
            
            
    if green_bin_sprite.colliderect(paper_bag_sprite):
        count = count + 1
        paper_bag_sprite.center = (2000, 2000)  
        dragging_paper_bag = False
        correct = py.mixer.music.load("dragon-studio-correct-472358.mp3")
        py.mixer.music.play(0)
        time.sleep(1)    
        score = score +1
    if green_bin_sprite.colliderect(bottle_sprite):
        count = count + 1
        bottle_sprite.center = (2000,2000)
        dragging_bottle = False
        correct = py.mixer.music.load("dragon-studio-correct-472358.mp3")
        py.mixer.music.play(0)
        time.sleep(1)

        score = score +1
    if green_bin_sprite.colliderect(newspaper_sprite):
        count = count + 1
        newspaper_sprite.center = (2000,2000)
        dragging_newspaper = False
        correct = py.mixer.music.load("dragon-studio-correct-472358.mp3")
        py.mixer.music.play(0)
        time.sleep(1)
        score = score +1 

    if green_bin_sprite.colliderect(foil_sprite):
        count = count + 1
        foil_sprite.center = (2000,2000)
        dragging_foil = False
        correct = py.mixer.music.load("logicallism-incorrect-buzzer-374194.mp3")
        py.mixer.music.play(0)
        time.sleep(1)
        score = score -1

    if green_bin_sprite.colliderect(banana_sprite):
            count = count + 1
            banana_sprite.center = (2000,2000)
            dragging_banana = False
            correct = py.mixer.music.load("logicallism-incorrect-buzzer-374194.mp3")
            py.mixer.music.play(0)
            time.sleep(1)
            score = score -1 

    if green_bin_sprite.colliderect(battery_sprite):
            count = count + 1
            battery_sprite.center = (2000,2000)
            dragging_battery = False
            correct = py.mixer.music.load("logicallism-incorrect-buzzer-374194.mp3")
            py.mixer.music.play(0)
            time.sleep(1)
            score = score -1 


    if red_bin_sprite.colliderect(paper_bag_sprite):
            count = count + 1
            paper_bag_sprite.center = (2000, 2000) 
            dragging_paper_bag = False
            correct = py.mixer.music.load("logicallism-incorrect-buzzer-374194.mp3")
            py.mixer.music.play(0)
            time.sleep(1)    
            score = score -1
    if red_bin_sprite.colliderect(bottle_sprite):
            count = count + 1
            bottle_sprite.center = (2000,2000)
            dragging_bottle = False
            correct = py.mixer.music.load("logicallism-incorrect-buzzer-374194.mp3")
            py.mixer.music.play(0)
            time.sleep(1)
            score = score -1
    if red_bin_sprite.colliderect(newspaper_sprite):
            count = count + 1
            newspaper_sprite.center = (2000,2000)
            dragging_newspaper = False
            correct = py.mixer.music.load("logicallism-incorrect-buzzer-374194.mp3")
            py.mixer.music.play(0)
            time.sleep(1)
            score = score -1 
    if red_bin_sprite.colliderect(foil_sprite):
            count = count + 1
            foil_sprite.center = (2000,2000)
            dragging_foil = False 
            correct = py.mixer.music.load("dragon-studio-correct-472358.mp3")
            py.mixer.music.play(0)
            time.sleep(1)
            score = score +1
    if red_bin_sprite.colliderect(banana_sprite):
                count = count + 1
                banana_sprite.center = (2000,2000)
                dragging_banana = False
                correct = py.mixer.music.load("dragon-studio-correct-472358.mp3")
                py.mixer.music.play(0)
                time.sleep(1)
                score = score +1 
    if red_bin_sprite.colliderect(battery_sprite):
                count = count + 1
                battery_sprite.center = (2000,2000)
                dragging_battery = False
                correct = py.mixer.music.load("dragon-studio-correct-472358.mp3")
                py.mixer.music.play(0)
                time.sleep(1)
                score = score +1 
    screen.fill("black")
    if count == 6:
        if score == 6:
            winner_text = font.render("well done, all correct" , True , "green")
            screen.blit(winner_text, (300,350))
        if score <6:
            incorrect_text = font.render("placed incorrectly" , True , "red")
            screen.blit(incorrect_text, (450, 500))
    score_text = font.render("score = " + str(score) , True, "green")
    instructions = font.render("drag the items to the correct bin" , True, "green")
    
   

    screen.blit(green_bin, green_bin_sprite)
    screen.blit(red_bin, red_bin_sprite)
    screen.blit(paper_bag, paper_bag_sprite)
    screen.blit(newspaper, newspaper_sprite)
    screen.blit(bottle, bottle_sprite)
    screen.blit(foil, foil_sprite)
    screen.blit(battery, battery_sprite)
    screen.blit(banana, banana_sprite)
    screen.blit(score_text, (300, 650))
    screen.blit(instructions, (35, 30))
    py.display.update()
py.quit()
