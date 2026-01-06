class Settings:
    """存储游戏的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1280
        self.screen_height = 960
        self.bg_color = (135, 206, 235)
        # self.bg_color = (255,255,255)

        # 飞船设置
        self.ship_speed = 1

        # 子弹设置
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
