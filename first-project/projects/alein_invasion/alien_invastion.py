import sys
import pygame

from settings import Settings


class AleinInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("外星入侵")

    def run_game(self):
        """开始游戏的主循环

        该方法包含游戏的事件处理和屏幕更新逻辑，
        通过无限循环维持游戏运行，处理退出事件，
        并以60FPS的帧率刷新游戏画面。
        """
        while True:
            # 处理游戏事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 填充背景颜色
            self.screen.fill(self.settings.bg_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()
            # 控制游戏帧率为60FPS
            self.clock.tick(60)


if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AleinInvasion()
    ai.run_game()
