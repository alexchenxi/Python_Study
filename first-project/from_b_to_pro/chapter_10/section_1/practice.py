# 10.1
from pathlib import Path

contents = (Path(__file__).parent / "learning_python.txt").read_text()
# print(contents)
paragraphs = contents.splitlines()

for paragraph in paragraphs:
    print(paragraph)


# 10.2

for paragraph in paragraphs:
    paragraph=paragraph.replace('Python','Javascript')
    print(paragraph)