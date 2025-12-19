# 10.11
import json
from pathlib import Path

# 定义常量避免重复计算
FAVORITE_NUMBER_FILE = Path(__file__).resolve().parent / "favorite_number.json"


def save_favorite_number():
    favorite_number = input("Enter favorite number: ")
    try:
        favorite_number = int(favorite_number)
    except ValueError:
        print("Please enter a number.")
        pass
    else:
        try:
            contents = json.dumps(favorite_number)
            FAVORITE_NUMBER_FILE.write_text(contents)
            print("Your favorite number is now stored in 'favorite_number.json'")
            return True  # 明确返回成功状态
        except Exception as e:
            print(f"Error saving favorite number: {e}")
            return False


def get_favorite_number():
    if FAVORITE_NUMBER_FILE.exists():
        try:
            contents = FAVORITE_NUMBER_FILE.read_text()
            favorite_number = json.loads(contents)
            print(f"I know your favorite number! It's {favorite_number}")
        except Exception as e:
            print(f"Error reading favorite number: {e}")
            print("Sorry I don't know your favorite number!")
    else:
        print("Sorry I don't know your favorite number!")


# get_favorite_number()


# 10.12
def get_favorite_number_final():
    if FAVORITE_NUMBER_FILE.exists():
        contents = FAVORITE_NUMBER_FILE.read_text()
        favorite_number = json.loads(contents)
        print(f"I know your favorite number! It's {favorite_number}")
    else:
        favorite_number = input("Enter favorite number: ")
        try:
            favorite_number = int(favorite_number)
        except ValueError:
            print("Please enter a number.")
            pass
        else:
            try:
                contents = json.dumps(favorite_number)
                FAVORITE_NUMBER_FILE.write_text(contents)
                print("Your favorite number is now stored in 'favorite_number.json'")
            except Exception as e:
                print(f"Error saving favorite number: {e}")


# get_favorite_number_final()

# 10.14


USERNAME_FILE = "username.json"


def get_stored_username(path):
    """获取已存储的用户名"""
    if not path.exists():
        return None
    try:
        contents = path.read_text(encoding="utf-8")
        data = json.loads(contents)
        # 确保必要字段存在且非空
        if isinstance(data, dict) and data.get("username"):
            return data
        else:
            return None
    except (json.JSONDecodeError, IOError) as e:
        # 捕获IO异常以增强鲁棒性
        print(f"Warning: Failed to read or decode file: {e}")
        return None


def get_new_username(path):
    """提示用户输入新用户名并保存"""
    username = input("Enter your username: ").strip()
    role = input("Enter your role: ").strip()
    age_input = input("Enter your age: ").strip()

    # 校验关键字段
    if not username:
        raise ValueError("Username cannot be empty.")
    try:
        age = int(age_input)
    except ValueError:
        raise ValueError("Age must be an integer.")

    user_info = {"username": username, "role": role, "age": age}

    contents = json.dumps(user_info)
    try:
        path.write_text(contents, encoding="utf-8")
    except IOError as e:
        print(f"Error writing to file: {e}")
        raise
    return username


def greet_user():
    """主交互流程"""
    base_path = Path(__file__).parent
    path = base_path / USERNAME_FILE

    user_info = get_stored_username(path)
    if user_info:
        # 询问当前用户是否为存储的用户
        confirm = (
            input(f"Is '{user_info['username']}' your username? (y/n): ")
            .lower()
            .strip()
        )
        if confirm in ["n", "no"]:
            # 用户否认，重新创建账户
            try:
                username = get_new_username(path)
                print(f"We'll remember you when you come back, {username}!")
            except Exception as e:
                print(f"Failed to save new user info: {e}")
        else:
            # 用户确认身份，显示欢迎信息
            print(f"Welcome back, {user_info['username']}!")
            print(
                f"You are a {user_info['role']} and you are {user_info['age']} years old."
            )
    else:
        # 没有找到旧记录，新建账户
        try:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
        except Exception as e:
            print(f"Failed to save new user info: {e}")


if __name__ == "__main__":
    greet_user()
