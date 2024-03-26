import pygame 

pygame.init()

screen = pygame.display.set_mode((600 , 300)) #flads = pygame.NOFRAME
running = True
pygame.display.set_caption("PyGame Fariza") #название файла
icon = pygame.image.load("images/icon-game-controller-b-1024.webp")
pygame.display.set_icon(icon) #иконка 

while running:

    pygame.display.update()

    for event in pygame.event.get(): # список из всех возможных знач 
        if event.type == pygame.QUIT: #выход из файла
                running = False 
                pygame.quit()
                

       
