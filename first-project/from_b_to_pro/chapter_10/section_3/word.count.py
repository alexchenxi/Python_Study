from pathlib import Path


def count_words(path):
    """计算一个文件多少个单词"""
    try:
        content = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ["alice.txt", "108heroes.txt", "notthere.txt"]
for file in filenames:
    path_abs = Path(__file__).parent / file
    count_words(path_abs)
