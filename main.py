"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one funny single-line excuse a developer gives
# when code breaks in production: "Never Tested as a User".
# The twist is that the code never broke — production simply ran it
# the way a real user would, which the developer never once did.
# One sentence, 114 characters — inside the 200-character gate.
import os

TEXT = (
    "The code didn\u2019t break in production \u2014 production just "
    "finally ran it the way a user would, which I never once did."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
