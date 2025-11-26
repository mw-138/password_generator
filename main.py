from random import randint, shuffle

import pyperclip

from config import Config

CHARACTERS: str = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*-_=+"
)


def get_password_length(min: int, max: int) -> int:
    try:
        return int(
            input(
                f"Enter password length (Leave empty for random length between {min}-{max}): "
            )
        )
    except ValueError:
        return randint(min, max)


def get_shuffled_characters(length: int) -> list[str]:
    chars = list(CHARACTERS)
    shuffle(chars)
    return chars[:length]


def main():
    cfg = Config.load()
    password_length = get_password_length(cfg.min_random_length, cfg.max_random_length)
    shuffled_characters = get_shuffled_characters(password_length)
    password = "".join(shuffled_characters)
    if cfg.copy_to_clipboard:
        pyperclip.copy(password)
        print(f"{password} copied to clipboard")
    else:
        print(password)
    cfg.save()


if __name__ == "__main__":
    main()
