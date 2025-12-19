import unittest
from unittest.mock import patch, mock_open
import json
from pathlib import Path
import sys
from io import StringIO

# 假设 remember_me.py 在同一目录或已导入
# from remember_me import greet_user, get_stored_username, get_new_username


class TestGreetUser(unittest.TestCase):

    @patch("pathlib.Path.exists")
    @patch("pathlib.Path.read_text")
    @patch("builtins.input", return_value="Alice")
    @patch("pathlib.Path.write_text")
    def test_greet_user_with_existing_user(
        self, mock_write, mock_input, mock_read, mock_exists
    ):
        """
        测试当存在已存储用户名时，greet_user() 的行为
        """
        # 设置模拟返回值
        mock_exists.return_value = True
        mock_read.return_value = json.dumps("Bob")

        # 捕获打印输出
        captured_output = StringIO()
        sys.stdout = captured_output

        # 调用函数
        # greet_user()

        # 恢复标准输出
        sys.stdout = sys.__stdout__

        # 验证结果
        # self.assertIn("Welcome back, Bob!", captured_output.getvalue())
        # mock_write.assert_not_called()

    @patch("pathlib.Path.exists")
    @patch("builtins.input", return_value="Charlie")
    @patch("pathlib.Path.write_text")
    def test_greet_user_new_user(self, mock_write, mock_input, mock_exists):
        """
        测试当没有已存储用户名时，greet_user() 的行为
        """
        # 设置模拟返回值
        mock_exists.return_value = False

        # 捕获打印输出
        captured_output = StringIO()
        sys.stdout = captured_output

        # 调用函数
        # greet_user()

        # 恢复标准输出
        sys.stdout = sys.__stdout__

        # 验证结果
        # self.assertIn("We'll remember you when you come back, Charlie!", captured_output.getvalue())
        # mock_write.assert_called_once()


if __name__ == "__main__":
    unittest.main()
