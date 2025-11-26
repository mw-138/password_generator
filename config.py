import json
from dataclasses import asdict, dataclass

SAVE_PATH: str = "config.json"


@dataclass
class Config:
    copy_to_clipboard: bool = True
    min_random_range: int = 10
    max_random_range: int = 20

    def save(self):
        with open(SAVE_PATH, "w") as f:
            json.dump(asdict(self), f, indent=2)

    @classmethod
    def load(cls):
        try:
            with open(SAVE_PATH, "r") as f:
                return cls(**json.load(f))
        except FileNotFoundError:
            new_config = cls()
            new_config.save()
            return new_config
