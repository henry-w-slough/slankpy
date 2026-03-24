
import json


def load_map(src:str) -> dict:
    try:
        with open(src) as data:
            return json.load(data)
    except Exception as e:
        print(f"ERROR: MapLoader: load_map: {e}")
        return {}