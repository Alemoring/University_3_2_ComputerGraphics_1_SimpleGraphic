import pygame
from pygame.color import THECOLORS

red = THECOLORS["red"]
blue = THECOLORS["blue"]
green = THECOLORS["green"]
black = THECOLORS["black"]
list_colors = [red, blue, green, black]

def start():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill(THECOLORS['white'])
    pygame.display.set_caption("First Lab")
    drawer = Drawer()
    run = True
    while run:
        if drawer.handle_events(screen) == False:
            run = False
        pygame.display.flip()
    pygame.quit()
    
def draw_shapes(screen):
    # Рисуем точку
    for i in range(len(list_colors)):
        rect = pygame.Rect(OX, OY, 100, 200)
        pygame.draw.rect(list_colors[i], rect)
    
class Drawer:
    def __init__(self):
        self.drawing = False
        self.last_pos = None
    def handle_events(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Левая кнопка мыши
                    print(event.pos)
                    self.drawing = True
                    self.last_pos = event.pos
                    rect = pygame.Rect(event.pos[0] - 50, event.pos[1] - 100, 100, 200)
                    pygame.draw.ellipse(screen, (255, 0, 0), rect)
                else:
                    screen.fill(THECOLORS['white'])
            # if event.type == pygame.MOUSEMOTION:
            #     if self.drawing:
            #         print("Draw")
            #         pygame.draw.line(screen, (0, 255, 0), self.last_pos, event.pos, 5) # Зеленая линия
            #         self.last_pos = event.pos
            # if event.type == pygame.MOUSEBUTTONUP:
            #     print("UP")
            #     if event.button == 1:
            #         self.drawing = False
            #     if event.button == 3:
            #         self.save_image(screen)
        return True
def save_image(self, screen):
    print('image saved')
    pygame.image.save(screen, "drawing.png")

start()
