"""Generate a secure random password.

Usage: python password_generator.py [length]
"""
import secrets
import string
import sys


def generate(length: int = 16) -> str:
    chars = string.ascii_letters + string.digits + "!@#$%^&*-_"
    return "".join(secrets.choice(chars) for _ in range(length))


if __name__ == "__main__":
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    print(generate(length))
