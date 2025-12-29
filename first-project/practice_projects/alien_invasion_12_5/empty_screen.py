import sys
import pygame
from pygame.display import set_caption


class EmptyScreen:
    def __init__(self):
        pygame.init()
        self.screen_width = 1080
        self.screen_height = 960
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Empty Screen")

    def run_game(self):
        """开始游戏的主循环

        该方法包含游戏的事件处理和屏幕更新逻辑，
        通过无限循环维持游戏运行，处理退出事件，
        并以60FPS的帧率刷新游戏画面。
        """
        try:
            while True:
                self._check_events()
                self.clock.tick(60)
        except Exception:
            # 确保在异常情况下也能正确清理资源
            pygame.quit()
            raise

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """响应按键"""
        print(event.key)
        if event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def __del__(self):
        """析构函数，确保资源被清理"""
        pygame.quit()


if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    es = EmptyScreen()
    es.run_game()
