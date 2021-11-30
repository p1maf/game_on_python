import pygame

class Ship:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('icon//1.svg')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def bltime(self):
        """"Ризует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)