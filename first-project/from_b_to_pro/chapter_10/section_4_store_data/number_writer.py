import json
from pathlib import Path

numbers = [2, 3, 5, 7, 11, 13]

path = Path(__file__).parent / "numbers.json"
contents = json.dumps(numbers)
path.write_text(contents, encoding="utf-8")
