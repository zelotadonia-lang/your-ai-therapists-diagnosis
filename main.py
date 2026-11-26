"""Entry for the "Your AI Therapist's Diagnosis" competition.

The competition gate requires the program to write a single text to
/output/entry.txt, 1-200 UTF-8 characters, not only whitespace.
The entry text is: Diagnosis: incognito guilt, cleared daily.
Your search history shows 'am I a bad person' at 2 a.m.
The program writes exactly that text, with no trailing newline.
The entry is 98 characters long, so the 1-200 character gate is met.
"""

import os

ENTRY = "Diagnosis: incognito guilt, cleared daily. Your search history shows 'am I a bad person' at 2 a.m."


def main():
    os.makedirs("/output", exist_ok=True)
    # Write exactly ENTRY, with no trailing newline.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
