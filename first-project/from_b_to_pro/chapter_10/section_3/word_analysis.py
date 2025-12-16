from pathlib import Path

txt_name = "alice.txt"

path = Path(__file__).parent / txt_name
try:
    content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = content.split()
    num_words = len(words)
    print(f"The file {txt_name} has about {num_words} words.")
