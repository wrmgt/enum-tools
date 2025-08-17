# Python enumeration tools for pentesting.


# DNS Enumerator

A simple Python script that queries common DNS record types for a given domain using [dnspython](https://www.dnspython.org/).

This tool is useful for quickly gathering information about a domain’s DNS configuration, such as IP addresses, mail servers, and text records.

---

## Features

- Queries the following DNS record types:
  - `A` (IPv4 addresses)
  - `AAAA` (IPv6 addresses)
  - `CNAME` (canonical name / alias)
  - `MX` (mail servers)
  - `TXT` (text records, including SPF/DKIM/DMARC)
  - `SOA` (start of authority)
- Uses `dnspython`, a widely used DNS toolkit for Python
- Simple and minimal codebase (easy to extend for additional record types)

---

## Requirements

- Python 3.8+
- [dnspython](https://pypi.org/project/dnspython/)

Install dependencies with:

```bash
pip install dnspython
```

If you're using a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Your requirements.txt should contain:
```
dnspython
```

## Usage

- After cloning install the requirements as described above.
- Edit the script at target_domain = 'google.com' for your domain.
- You can also modify the record_types list to add or remove record types.

## Roadmap

- Add CLI argument parsing (--domain, --types)
- Support for JSON/CSV output
- Retry and timeout configuration via CLI flags
