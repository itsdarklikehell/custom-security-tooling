"""Simple auth-log analyzer."""
import argparse, re
from collections import Counter

FAILED_RE = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")


def analyze(path: str) -> dict:
    ips = Counter()
    total = 0
    with open(path) as f:
        for line in f:
            m = FAILED_RE.search(line)
            if m:
                ips[m.group(1)] += 1
                total += 1
    return {"failed_attempts": total, "top_ips": ips.most_common(5)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--file", required=True)
    args = p.parse_args()
    print(analyze(args.file))


if __name__ == "__main__":
    main()
