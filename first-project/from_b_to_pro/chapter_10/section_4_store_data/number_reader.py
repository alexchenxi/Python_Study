import json
from pathlib import Path

path = Path(__file__).parent / "numbers.json"
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)
