"""Count words, lines, and the most common words in a text file.

Usage: python word_counter.py file.txt [top_n]
"""
import re
import sys
from collections import Counter


def analyze(text: str, top_n: int = 10) -> None:
    words = re.findall(r"[a-zA-Z']+", text.lower())
    print(f"Lines: {len(text.splitlines())}")
    print(f"Words: {len(words)}")
    print(f"Unique words: {len(set(words))}")
    print(f"\nTop {top_n} words:")
    for word, count in Counter(words).most_common(top_n):
        print(f"  {word}: {count}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        analyze(f.read(), int(sys.argv[2]) if len(sys.argv) > 2 else 10)
