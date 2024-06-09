# імпорт бібліотеки pygame
import pygame
pygame.init()
from random import randint 

class Player(): # клас для створення шаблону персонажа
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect() # "межі" персонажа
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висота

#зони спавну персонажа
left = [[-200,-100], [0,400]]
up = [[0,400], [-200,-100]]
right = [[600,700],[0,400]]
down = [[0,400],[-200,100]]

#змінні відповідальні за рух
dx = 20
dy = 0

# створення головного вікна
window = pygame.display.set_mode((500, 500))

# створення персонажа
# player - назва об'єкту персонажа (може бути змінена)
#              ( x    y  width height    'name_image')         
player = Player(100, 100, 100, 100, 'jupiter.png')

# кольори
white = (255, 255, 255)
black = (0, 0, 0)
# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

# головний цикл гри
game = True
while game:
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    # відображення персонажа на екрані
    window.blit(player.image, (player.rect.x, player.rect.y))  

    if player.rect.x > 500 or player.rect.x < -100 or player.rect.y > 500 or player.rect.y < -100:
        n = randint(0,5) #випадково обрали зону
        
        if n == 0:
            player.rect.x = randint(left[0][0], left[0][1])
            player.rect.y = randint(left[1][0], left[1][1])
            dx = 10
            dy = 0
        if n == 1:
            player.rect.x = randint(up[0][0], up[0][1])
            player.rect.y = randint(up[1][0], up[1][1])
            dx = 0
            dy = -10
        if n == 2:
            player.rect.x = randint(right[0][0], right[0][1])
            player.rect.y = randint(right[1][0], right[1][1])
            dx = -10
            dy = 0
        if n == 3:
            player.rect.x = randint(down[0][0], down[0][1])
            player.rect.y = randint(down[1][0], down[1][1])
            dx = 0
            dy = 10

    player.rect.x += dx 
    player.rect.y += dy

    # задання частоти кадрів та оновлення екрану
    clock.tick(30)
    pygame.display.update()

pygame.quit()