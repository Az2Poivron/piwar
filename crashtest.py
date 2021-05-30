import pygame
import settings
class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.WINDOWS_NAME)
        self.width = settings.WIDTH
        self.height = settings.HEIGHT
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.bg = pygame.image.load('source/assets/images/backgrounds/menu.jpg')
        self.bg = pygame.transform.scale(self.bg , (self.width,self.height))
        self.screen.blit(self.bg, (0,0))
        pygame.display.update()

game = Game()

running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()

