# Custom Security Tooling

A collection of purpose-built Python security tools: small, focused utilities for tasks like password auditing, hash cracking helpers, payload generation, and log analysis. Each tool is standalone and runnable.

## Tools

- `tools/password_audit.py` - Password strength and policy checker
- `tools/hash_identifier.py` - Identify hash types by format
- `tools/payload_gen.py` - Generate common test payloads
- `tools/log_analyzer.py` - Parse and summarize security logs

## Installation

```bash
git clone https://github.com/itsdarklikehell/custom-security-tooling.git
cd custom-security-tooling
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python tools/password_audit.py --password "hunter2"
python tools/hash_identifier.py --hash "5f4dcc3b5aa765d61d8327deb882cf99"
python tools/payload_gen.py --type xss
python tools/log_analyzer.py --file auth.log
```

## Disclaimer

For authorized testing and education only.

## License

MIT License. See [LICENSE](LICENSE).
