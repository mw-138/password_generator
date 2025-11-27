import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PasswordExporter:
    _file_path: str = "export.csv"

    @classmethod
    def get_rows(cls) -> list[dict]:
        if not Path(cls._file_path).exists():
            return []

        with open(cls._file_path, "r", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)

    @classmethod
    def export(cls, password: str, identifier: str = "") -> None:
        file_exists = Path(cls._file_path).exists()

        with open(cls._file_path, "a", newline="") as f:
            writer = csv.writer(f)

            identifier = (
                identifier != "" and identifier or f"password_{len(cls.get_rows()) + 1}"
            )

            if not file_exists:
                writer.writerow(["identifier", "password"])

            writer.writerow([identifier, password])
