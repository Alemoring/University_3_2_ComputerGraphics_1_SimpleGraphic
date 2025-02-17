import pygame
from pygame.color import THECOLORS
from datetime import datetime

red = THECOLORS["red"]
blue = THECOLORS["blue"]
green = THECOLORS["green"]
black = THECOLORS["black"]
list_colors = [red, blue, green, black]
# ellips_color = (100, 100, 100)


def start():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.get_size()
    screen.fill(THECOLORS['white'])
    pygame.display.set_caption("First Lab")
    drawer = Drawer()
    run = True
    draw_colour = True
    while run:
        if draw_colour:
            draw_shapes(screen)
            draw_colour = False
        if drawer.handle_events(screen) == False:
            run = False
        pygame.display.flip()
    pygame.quit()
    
def draw_shapes(screen):
    # Рисуем разноцветные квадратики
    OX = 0
    OY = 0
    for i in range(len(list_colors)):
        rect = pygame.Rect(OX, OY, 50, 50)
        pygame.draw.rect(screen, list_colors[i], rect)
        OX += 50
    
class Drawer:
    def __init__(self):
        self.drawing = False
        self.last_pos = None
        self.ellips_color = (100, 100, 100)
    def handle_events(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Левая кнопка мыши
                    if event.pos[1] > 50 or event.pos[0] > 50 * len(list_colors):
                        self.drawing = True
                        self.last_pos = event.pos
                        rect = pygame.Rect(event.pos[0] - 50, event.pos[1] - 100, 100, 200)
                        pygame.draw.ellipse(screen, self.ellips_color, rect)
                    self.ellips_color = screen.get_at(event.pos)
                else:
                    # save_image(screen)
                    screen.fill(THECOLORS['white'])
                    draw_shapes(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                    save_image(screen)
        return True

def save_image(screen):
    postfix = str(datetime.now().year) + "_" + str(datetime.now().month) + "_" + str(datetime.now().day) + "-" + str(datetime.now().hour) + "_" + str(datetime.now().minute) + "_" + str(datetime.now().second) + ".png" 
    image = screen.subsurface((0, 50, (screen.get_size())[0], (screen.get_size())[1] - 50)) 
    pygame.image.save(image, "pygame_" + postfix)
    print('image saved')

start()
