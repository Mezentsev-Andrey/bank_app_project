from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT_PATH, 'data')
JSON_PATH = Path.joinpath(DATA_PATH, 'operations.json')