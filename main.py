"""The Dog Reviews the Mailman — one-line review, written by the dog."""

import os


def dog_review():
    """The review itself: a grievance, a smell, and a small triumph."""
    return (
        "One star. He comes every day, smells of a hundred other dogs, "
        "and leaves without once throwing the ball \u2014 so I barked until "
        "he ran away, and honestly, I consider that a win."
    )


def resolve_entry_path():
    """Pick where entry.txt goes.

    ENTRY_OUT may name a file or a directory; then MAKEFUN_OUTPUT_DIR;
    then the grader's /output/entry.txt; cwd only as a last resort.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out) or entry_out.endswith(os.sep):
            return os.path.join(entry_out, "entry.txt")
        return entry_out
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def write_entry():
    """Write the review with no trailing newline; fall back to cwd."""
    text = dog_review()
    path = resolve_entry_path()
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
    except OSError:
        path = os.path.join(os.getcwd(), "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
    return path


if __name__ == "__main__":
    write_entry()
