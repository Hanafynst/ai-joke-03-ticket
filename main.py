import os

JOKE = (
    "I asked my coding agent to fix the login bug. It opened a ticket, "
    "wrote a root-cause analysis, estimated three story points, "
    "and assigned it back to me."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
