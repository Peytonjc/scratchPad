import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Scratch Pad Display")
icon = pygame.image.load('square.png')
pygame.display.set_icon(icon)

r = 0
g = 255
b = 0
rd = 1
gd = 1
bd = 1
playX = 270
playY = 350
size = 10
leftDown = False

def player(x, y):
    screen.blit(icon, (x, y))


screen.fill((0, 150, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            size = size + 1
        if (event.key == pygame.K_DOWN) & (size > 0):
            size = size - 1
        if event.key == pygame.K_1:
            r = 255
            g = 0
            b = 0
        if event.key == pygame.K_2:
            r = 0
            g = 255
            b = 0
        if event.key == pygame.K_3:
            r = 0
            g = 0
            b = 255

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == pygame.BUTTON_LEFT:
            leftDown = True
            mousex, mousey = event.pos
            pygame.draw.circle(screen, (r, g, b), (mousex, mousey), size, 0)
            pygame.display.update()
        if event.button == pygame.BUTTON_RIGHT:
            screen.fill((0, 150, 255))
            pygame.display.update()

    if (event.type == pygame.MOUSEMOTION) & (leftDown):
        mousex, mousey = event.pos
        pygame.draw.circle(screen, (r, g, b), (mousex, mousey), size, 0)
        pygame.display.update()

        #time.sleep(1)
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == pygame.BUTTON_LEFT:
            leftDown = False


    #player(playX, playY)
    pygame.display.update()
