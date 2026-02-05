import json
from typing import Any, Dict


class JsonManager:
    """
    Context manager for reading and writing JSON configuration files.
    """

    def __init__(self, path: str):
        self.path = path
        self.config = {}

    def __enter__(self) -> Dict[str]:
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.config = {}
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.config, file, indent=4, ensure_ascii=False)


config_path = "config.json"

with JsonManager(config_path) as config:
    config["app_name"] = "MyApp"
    config["version"] = "1.0"
    config["debug"] = True
