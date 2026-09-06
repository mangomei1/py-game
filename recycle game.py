import pygame as py
py.init()
running = True
screen = py.display.set_mode((700, 700))
py.display.set_caption("recycle game")
running = True

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
dragging_bottle= False

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.fill("black")
   

    screen.blit(green_bin, green_bin_sprite)
    screen.blit(red_bin, red_bin_sprite)
    screen.blit(paper_bag, paper_bag_sprite)
    screen.blit(newspaper, newspaper_sprite)
    screen.blit(bottle, bottle_sprite)
    screen.blit(foil, foil_sprite)
    screen.blit(battery, battery_sprite)
    screen.blit(banana, banana_sprite)
    py.display.update()
py.quit()
