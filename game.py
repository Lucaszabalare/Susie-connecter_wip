import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "Susie Connect"

start_time = 0
total_time = 0
number_of_cats = 10
current_cat = 0

cats = []
lines = []

def creat_cats():
    global start_time
    for i in range(number_of_cats):
        susie = Actor("susie")
        susie.pos = randint(40,750),randint(40,550)
        cats.append(susie)
    start_time = time()

def draw():
    global total_time
    screen.blit("space",(0,0))

    num = 1
    for susie in cats:
        screen.draw.text(str(num),(susie.pos[0],susie.pos[1] + 30))
        susie.draw()
        num = num + 1
    
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    
    if current_cat < number_of_cats:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)),(15,15),fontsize = 30)
    else:
        screen.draw.text(str(round(total_time,1)),(15,15),fontsize = 30)
    
    

def update():
    pass

def on_mouse_down(pos):
    global current_cat, lines
    if current_cat < number_of_cats:
        if cats[current_cat].collidepoint(pos):
            if current_cat:
                lines.append((cats[current_cat - 1].pos , cats[current_cat].pos))
            current_cat = current_cat + 1
        else:
            lines = []
            current_cat = 0

creat_cats()
pgzrun.go()
        