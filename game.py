import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "Susie Connect"

start_time = 0
total_time = 0
end_time = 0
number_of_cats = 10
next_cat = 0

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
        screen.draw.text(str(num),(susie.pos[0],susie.pos[1] + 20))
        susie.draw()
        num = num + 1
    



creat_cats()
pgzrun.go()
        