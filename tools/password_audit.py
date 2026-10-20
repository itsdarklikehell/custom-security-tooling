"""Password strength checker."""
import argparse, re, sys


def check(password: str) -> dict:
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[^A-Za-z0-9]", password): score += 1
    levels = ["very weak", "weak", "fair", "good", "strong", "very strong"]
    return {"password": password, "score": score, "rating": levels[min(score, len(levels)-1)]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--password", required=True)
    args = p.parse_args()
    print(check(args.password))


if __name__ == "__main__":
    main()
