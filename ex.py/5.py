import pygame

pygame.init()

screen = pygame.display.set_mode((1500,1500))
run = True

square = pygame.Surface((100 , 170))  # поверхность 
square.fill((222, 53, 197))
myfont = pygame.font.Font('front/Rubik_Scribble-2/RubikScribble-Regular.ttf' , 80) 
text_surface = myfont.render('Fariza' , True ,'Blue' )
photo = pygame.image.load("images/1337497_game_go_play_pikachu_pokemon_icon.png")
back_ground = False
clock = pygame.time.Clock()

while run :
    pygame.draw.circle(screen , 'Red' , (10 ,10) , 20)

    screen.blit(square , (10,0))
    screen.blit(text_surface , (300, 100))
    screen.blit(photo, (150,150))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if back_ground: clock = (222, 53, 197)
pygame.quit()