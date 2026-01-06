from pathlib import Path
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load(Path(__file__).parent / "images/alien.jpeg")
        self.image = pygame.transform.scale(self.image, (80, 64))  # 缩放图像
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)  # 添加y坐标的浮点数版本，用于精确移动

    def update(self):
        """移动外星人"""
        # 垂直移动 - 持续向下移动
        self.y += self.settings.alien_speed
        self.rect.y = self.y

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
