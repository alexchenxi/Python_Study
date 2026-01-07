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
        self.rect = self.image.get_rect()
        self.bg_color = ai_game.settings.bg_color

        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性 x 中存储一个浮点数
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # 移动速度
        self.moving_speed = self.settings.ship_speed

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.moving_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.moving_speed

        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
