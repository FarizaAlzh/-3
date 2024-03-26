import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((512, 512))
screen.fill((255, 255, 255))

index = 0
playlist = [
    r"/Users/fariza/Desktop/WG7n2qH1dL9bg7SR.mp3",
    r"/Users/fariza/Desktop/Glass Animals-Heat Waves.mp3",
    r"/Users/fariza/Desktop/Calvin_Harris-My_Way.mp3",
    r"/Users/fariza/Desktop/Intelligency-Август.mp3",
]

pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play()

run = True
paused = False

while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused

            elif event.key == pygame.K_UP:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_DOWN:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

