# Python enumeration tools


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



# Subdomain Enumerator (Multithreaded)

This Python tool performs fast subdomain enumeration by attempting HTTP connections to potential subdomains of a given target domain.
It uses multithreading to speed up discovery and saves the results to a file.

---

## Features
- Uses a wordlist (`subdomains.txt`) to test potential subdomains.
- Multithreaded for faster execution.
- Saves all discovered subdomains to `discovered_subdomains.txt`.

---

## Requirements
- Python 3.7+
- The following Python libraries:
  - `requests`

Install dependencies with:

```bash
pip install -r requirements.txt
```
Your requirements.txt should contain:

```
requests
```

## Usage

- Clone this repo or download the script.
- Adjust the value of youtube.com to whatever the domain is you want to target.
- Double check your .venv and activate it and install dependencies.
- Run the script.
  ```bash
  python3 subdomain_enum.py
  ```
  - Discovered subdomains will be printed to the console and saved into discovered_subdomains.txt
