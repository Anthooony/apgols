import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

t_m = [
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1]
    ]
t_m2 = [
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0]
    ]

while running==True:
    cellSize = 800/len(t_m2)

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for y in range(len(t_m2)):
        for x in range(len(t_m2[y])):
            if t_m2[x][y]==0:
                pygame.draw.rect(screen, "black", [y*cellSize, x*cellSize, cellSize, cellSize])
            else:
                pygame.draw.rect(screen, "white", [y*cellSize, x*cellSize, cellSize, cellSize])

    pygame.display.flip()
    clock.tick(60)
    