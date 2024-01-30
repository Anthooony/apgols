import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

running = True
dragging = False
zoom = 1
cam=[0, 0]

while running==True:

    screen.fill("black")

    matrix=[[random.choice([".", "O"]) for i in range(24)] for h in range(24)]      #the update method will have to be in the pygame loop
    
    cellSize = int((screen.get_size()[0]/len(matrix))*zoom)
    
    if dragging:
        relx, rely = pygame.mouse.get_rel()
        cam[0] += relx
        cam[1] += rely

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 4 or event.button == 5:
                zoom *= 1.25 if event.button == 4 else 0.75

            if event.button == 1:
                if pygame.mouse.get_focused():
                    pygame.mouse.get_rel()
                    dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False


    
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[x][y] == ".":
                pygame.draw.rect(screen, "black", [y*cellSize+cam[0], x*cellSize+cam[1], cellSize, cellSize]) #look into why x and y are reversed
            else:
                pygame.draw.rect(screen, "white", [y*cellSize+cam[0], x*cellSize+cam[1], cellSize, cellSize])

    
    pygame.display.flip()
    clock.tick(60)
    
