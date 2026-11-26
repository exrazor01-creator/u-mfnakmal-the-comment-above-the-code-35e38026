"""The Comment Above the Code -- make.fun one-liner entry.

The line is a comment a developer would leave above fragile production
code, in the voice of someone who has already learned the lesson the
hard way. The joke is specific, not generic: a single sleep(1) call
that nobody understands but that checkout somehow depends on. The
developer tried removing it twice and production broke both times, so
the comment is not a warning about theory -- it is a scar, written
down so the next person does not repeat the experiment. The humour
lands in one beat: the most load-bearing line in the codebase is a
one-second nap, and the punchline is the honest admission that nobody
knows why it works, only that it does.
"""

import os

# The entry: a developer's comment above fragile production code.
# A sleep(1) nobody understands holds checkout together. Removing it
# was tried twice, and it broke both times -- so the comment begs the
# next reader not to be the third attempt.
LINE = "// Do not remove this sleep(1). We tried twice. Checkout broke both times. Nobody knows why."


def validate(text):
    """Check that a candidate entry line meets the competition rules.

    Raises ValueError unless ``text`` is a non-blank single-line ASCII
    string of 1 to 200 characters, with no leading or trailing space and
    no double spaces.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
