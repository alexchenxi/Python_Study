class Settings:
    """存储游戏的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1280
        self.screen_height = 960
        self.bg_color = (135, 206, 235)

        # 飞船设置
        self.ship_speed = 10

        # 子弹设置
        self.bullet_speed = 20
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
