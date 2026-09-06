import pygame as py
import time
py.init()
running = True
screen = py.display.set_mode((700,700))
py.display.set_caption("birthday card")


smile_image= py.image.load("smiley face.jpeg")
smile_image = py.transform.scale(smile_image, (700,700))
cake_image= py.image.load("birthday.jpeg")
cake_image = py.transform.scale(cake_image, (700,700))
balloons_image= py.image.load("balloons.jpeg")
balloons_image = py.transform.scale(balloons_image, (700,700))
popper_image= py.image.load("party popper.jpg")
popper_image = py.transform.scale(popper_image, (700,700))
py.mixer.init()
birthdaysong = py.mixer.music.load("birthdaysong.mp3")
py.mixer.music.play(-1)


font = py.font.Font(None, 36)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False 
    screen.fill("black")
    text1 = font.render("happy birthday" , True, "green")
    text2 = font.render("have a good day" , True, "green")
    text3 = font.render("have a nice year" , True, "green")
    text4 = font.render("time to celebrate" ,  True, "green")   

    screen.blit(smile_image, (0, 0))
    screen.blit(text1)
    py.display.update()
    time.sleep(2)
    screen.fill("black")
    screen.blit(cake_image, (0, 0))
    screen.blit(text2)
    py.display.update()
    time.sleep(2)
    screen.fill("black")
    screen.blit(balloons_image, (0, 0))
    screen.blit(text3)
    py.display.update()
    time.sleep(2)
    screen.fill("black")
    screen.blit(popper_image, (0, 0))
    screen.blit(text4)
    py.display.update()
    time.sleep(2)
py. quit()
