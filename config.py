import json
from dataclasses import asdict, dataclass

SAVE_PATH: str = "config.json"


@dataclass
class Config:
    copy_to_clipboard: bool = True
    min_random_length: int = 10
    max_random_length: int = 20
    include_lowercase: bool = True
    include_uppercase: bool = True
    include_numbers: bool = True
    include_symbols: bool = True

    def save(self):
        with open(SAVE_PATH, "w") as f:
            json.dump(asdict(self), f, indent=2)

    @classmethod
    def load(cls):
        try:
            with open(SAVE_PATH, "r") as f:
                return cls(**json.load(f))
        except FileNotFoundError:
            return cls()
