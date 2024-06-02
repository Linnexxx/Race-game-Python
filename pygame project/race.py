import pygame, random
import time

pygame.init()

width =800

height = 600

bg = pygame.image.load('images/road.png')
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

exit = True
bg_y = 0

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, new_image, x, y, width, height) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(new_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def show(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Car(GameSprite):
    def __init__(self, new_image, x, y, width, height, speed) -> None:
        super().__init__(new_image, x, y, width, height)
        self.width = width
        self.speed = speed
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < width - self.width:
            self.rect.x += self.speed

class Obstacle(GameSprite):
    def __init__(self, new_image, x, y, width, height, speed) -> None:
        super().__init__(new_image, x, y, width, height)
        self.speed = speed
        self.height = height
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= height + self.height:
            self.kill()

obstacles = pygame.sprite.Group()
coor_line = [140, 260, 380, 530]

delay_time = 2
last_spawn = 0

player = Car('images/car.png', width / 2, height - 170, 170, 170, 10)

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y - 600))
    if time.time() - last_spawn > delay_time:
        last_spawn = time.time()
        for _ in range(random.randint(1, 3)):
            obstacles.add(Obstacle('images/car.png', random.choice(coor_line), 0 - 100, 100, 100, 5))
    obstacles.update()
    player.update()
    player.show()
    obstacles.draw(screen)
    pygame.display.update()
    clock.tick(30)
    bg_y += 8
    if bg_y == 600:
        bg_y = 0