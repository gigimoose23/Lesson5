import pgzrun
import time
import random

startTime = 0
endTime = 38
totalTime = 0

WIDTH = 800
HEIGHT = 600

satellites = []
lines = []
nextSatellite = 0

numberOfSatellites = 10

def drawSatellite():
    global startTime
    for i in range(numberOfSatellites):
        Satellite = Actor("satellite")
        Satellite.pos = (random.randint(50,600), random.randint(50,600))
        satellites.append(Satellite)
    startTime = time.time()
def draw():
    global totalTime
    if nextSatellite < numberOfSatellites:
        totalTime = round(time.time() - startTime)
    screen.blit("background", (0,0))
    indexVariable = 1
    screen.draw.text(str(totalTime), color=(255,255,255), pos=(5,5))
    for object in satellites:
        screen.draw.text(str(indexVariable), (object.pos[0] - 3, object.pos[1] + 15))
        object.draw()
        indexVariable += 1
    for line in lines:
        screen.draw.line(line[0],line[1], (255,255,255))


drawSatellite()

def update():
    pass

def on_mouse_down(pos):
    global nextSatellite,lines
    
    if nextSatellite < numberOfSatellites:
        if satellites[nextSatellite].collidepoint(pos):
            if nextSatellite > 0:
                lines.append((satellites[nextSatellite - 1].pos, satellites[nextSatellite].pos))
            
            nextSatellite += 1
        else:
            lines = []
            nextSatellite = 0
pgzrun.go()

