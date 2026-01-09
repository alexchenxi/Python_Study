import os


class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # 定义最高分文件路径（保存在当前文件夹中）
        self.high_score_file = os.path.join(os.path.dirname(__file__), "high_score.txt")

        # 从文件中读取最高分
        self._load_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """从文件中读取最高分"""
        try:
            if os.path.exists(self.high_score_file):
                with open(self.high_score_file, "r", encoding="utf-8") as file:
                    content = file.read().strip()
                    if content:
                        self.high_score = int(content)
            else:
                self.high_score = 0
        except ValueError:
            self.high_score = 0
        except Exception as e:
            self.high_score = 0
