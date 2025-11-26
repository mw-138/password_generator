from random import randint, shuffle

import pyperclip

from config import Config

CHARACTERS: str = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!?^&%$£@#"
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
    loaded_config = Config.load()
    password_length = get_password_length(
        loaded_config.min_random_length, loaded_config.max_random_length
    )
    chosen_characters = get_shuffled_characters(password_length)
    password = "".join(chosen_characters)
    if loaded_config.copy_to_clipboard:
        pyperclip.copy(password)
        print(f"{password} copied to clipboard")
    else:
        print(password)
    loaded_config.save()


if __name__ == "__main__":
    main()
