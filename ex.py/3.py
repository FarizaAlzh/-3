import pygame 

pygame.init()

screen = pygame.display.set_mode((600 , 300)) #flads = pygame.NOFRAME
running = True
pygame.display.set_caption("PyGame Fariza") #название файла
icon = pygame.image.load("images/icon-game-controller-b-1024.webp")
pygame.display.set_icon(icon) #иконка 

while running:
    #screen.fill((106, 138, 81))

    pygame.display.update()

    for event in pygame.event.get(): # список из всех возможных знач 
        if event.type == pygame.QUIT: #выход из файла
                running = False 
                pygame.quit()
        elif event.type == pygame.KEYDOWN:#если нажмем на кнопку а 
             if event.key == pygame.K_a:
                  screen.fill((138, 56, 126))

       
