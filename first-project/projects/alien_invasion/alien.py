from pathlib import Path
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        super().__init__()
        # 将传入的ai_game对象的screen属性赋值给当前对象的screen属性
        # 用于在当前类实例中保存游戏屏幕的引用，以便后续在类的方法中使用屏幕对象进行绘制等操作
        self.screen = ai_game.screen

        self.image = pygame.image.load(Path(__file__).parent / "images/alien.jpeg")
        self.image = pygame.transform.scale(self.image, (80, 64))  # 缩放图像
        # 获取图像的矩形边界框，用于碰撞检测和位置控制
        self.rect = self.image.get_rect()
        # 设置矩形对象的位置坐标，将x坐标设置为矩形的宽度值，y坐标设置为矩形的高度值
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
