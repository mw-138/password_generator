import json
from dataclasses import asdict, dataclass


@dataclass
class Config:
    _file_path: str = "config.json"
    copy_to_clipboard: bool = True
    min_random_length: int = 10
    max_random_length: int = 20
    include_lowercase: bool = True
    include_uppercase: bool = True
    include_numbers: bool = True
    include_symbols: bool = True
    export_to_file: bool = True

    def save(self):
        with open(self._file_path, "w") as f:
            json.dump(asdict(self), f, indent=2)

    @classmethod
    def load(cls):
        try:
            with open(cls._file_path, "r") as f:
                return cls(**json.load(f))
        except FileNotFoundError:
            return cls()
