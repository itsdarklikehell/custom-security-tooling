"""Hash type identifier by format."""
import argparse, re

PATTERNS = [
    (r"^[a-f0-9]{32}$", "MD5"),
    (r"^[a-f0-9]{40}$", "SHA-1"),
    (r"^[a-f0-9]{64}$", "SHA-256"),
    (r"^[a-f0-9]{128}$", "SHA-512"),
    (r"^\$2[aby]\$.{56}$", "bcrypt"),
]


def identify(h: str) -> str:
    h = h.strip().lower()
    for pat, name in PATTERNS:
        if re.match(pat, h):
            return name
    return "unknown"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--hash", required=True)
    args = p.parse_args()
    print(identify(args.hash))


if __name__ == "__main__":
    main()
