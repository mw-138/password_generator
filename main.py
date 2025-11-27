import string
from random import randint, shuffle

import pyperclip

from config import Config


def get_characters(
    include_lowercase: bool = True,
    include_uppercase: bool = True,
    include_numbers: bool = True,
    include_symbols: bool = True,
) -> str:
    chars = ""
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += "!@#$%^&*-_=+"

    return chars


def get_password_length(min: int, max: int) -> int:
    try:
        return int(
            input(
                f"Enter password length (Leave empty for random length between {min}-{max}): "
            )
        )
    except ValueError:
        return randint(min, max)


def get_shuffled_characters(characters: str, length: int) -> list[str]:
    chars = list(characters)
    shuffle(chars)
    return chars[:length]


def main():
    cfg = Config.load()
    password_length = get_password_length(cfg.min_random_length, cfg.max_random_length)
    shuffled_characters = get_shuffled_characters(
        get_characters(
            cfg.include_lowercase,
            cfg.include_uppercase,
            cfg.include_numbers,
            cfg.include_symbols,
        ),
        password_length,
    )
    password = "".join(shuffled_characters)
    if cfg.copy_to_clipboard:
        pyperclip.copy(password)
        print(f"{password} copied to clipboard")
    else:
        print(password)
    cfg.save()


if __name__ == "__main__":
    main()
