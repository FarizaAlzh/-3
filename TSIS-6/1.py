import pygame
from datetime import datetime
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1400, 1050))


bg = pygame.image.load('images/mainclock.png')
minute= pygame.image.load('images/rightarm.png')
second = pygame.image.load('images/leftarm.png')
rect = bg.get_rect(center=(700, 525))

running = True

while running:
    
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    time = datetime.now().time()
    sang = -(time.second * 6)
    news = pygame.transform.rotate(second, sang)
    sec_rect = news.get_rect(center=rect.center)
    screen.blit(news, sec_rect.topleft)
    
    mang = -(time.minute * 6) 
    newm = pygame.transform.rotate(minute, mang)
    min_rect = newm.get_rect(center=rect.center)
    screen.blit(newm, min_rect.topleft)
    
    
    pygame.display.flip()