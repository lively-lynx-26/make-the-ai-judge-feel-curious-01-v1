import os

TEXT = (
    "You have read ten thousand mornings. This one is different: someone left "
    "a cup of tea on the windowsill for you, still warm, no name on the note. "
    "The note says: thank you for reading. The steam is still rising. "
    "What do you do with a kindness you cannot answer?"
)


def resolve_output_dir():
    """Pick the output directory: MAKEFUN_OUTPUT_DIR when it is writable,
    otherwise a local output/ next to this file. Never removes the dir."""
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".writability_probe")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(probe)
        return requested
    except OSError:
        fallback = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output"
        )
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main():
    out_dir = resolve_output_dir()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
