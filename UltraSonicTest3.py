import pygame
from pygame.locals import *
from SonicSensor import *

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode ((width, height))

screen.fill (0xFFFFFF)

sensor = SonicSensor ("banana", 23, 24)

running = True
count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    distance = sensor.PingInch ()
    print ("{} Distance inches: {}".format (count, sensor.PingInch ()))
    
    colorOffset = int(distance) * 10
    if colorOffset > 255:
        colorOffset = 255
    color = (255-colorOffset, colorOffset, 0)
    
    screen.fill (color)
    pygame.display.update ()

    time.sleep (0.015)

    count += 1
