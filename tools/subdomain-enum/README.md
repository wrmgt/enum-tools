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
