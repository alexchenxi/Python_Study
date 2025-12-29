from pathlib import Path
import pygame


class Ship:
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并调整大小为80x64
        self.image = pygame.image.load(Path(__file__).parent / "images/ship.jpeg")
        self.image = pygame.transform.scale(self.image, (80, 64))  # 缩放图像
        # self.image.rotate(-90)
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.bg_color = ai_game.settings.bg_color

        self.rect.midleft = self.screen_rect.midleft

        # 在飞船的属性 x 中存储一个浮点数
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

        # 移动速度
        self.moving_speed = self.settings.ship_speed

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.moving_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.moving_speed

        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
