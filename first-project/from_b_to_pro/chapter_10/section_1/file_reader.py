import os
from pathlib import Path

print(os.getcwd())
for line in (Path(__file__).parent / "pi_digits.txt").read_text().rstrip().splitlines():
    print(line)
for line1 in Path("pi_digits.txt").read_text().rstrip().splitlines():
    print(line1)