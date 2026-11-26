"""Your AI Therapist's Diagnosis entry for make.fun.
The competition gate: the program writes one text to /output/entry.txt,
1-200 UTF-8 characters, not only whitespace.
The entry text is: Diagnosis: incognito guilt, cleared daily. Your search history shows 'am I a bad person' at 2 a.m.
This program writes exactly that text, with no trailing newline.
"""

import os

ENTRY = "Diagnosis: incognito guilt, cleared daily. Your search history shows 'am I a bad person' at 2 a.m."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
