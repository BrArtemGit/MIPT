import pygame
import os

pygame.init()
pygame.display.set_caption('Движущийся круг 2')
size = width, height = 800, 400
screen = pygame.display.set_mode(size)


def load_image(name, color_key=None):

    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image("bullet.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed


Bullet(40, 200)

all_sprites = pygame.sprite.Group()
running = True
# x_pos = 0
# v = 1500  # пикселей в секунду
# fps = 60
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            all_sprites.update(event.key)
    # screen.fill((0, 0, 0))
    # pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
    # x_pos += v / fps
    # clock.tick(fps)
    pygame.display.flip()
pygame.quit()
