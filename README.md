
# 🕵️ OSINT-FRAMEWORK

A beginner-friendly OSINT (Open-Source Intelligence) framework script that helps security researchers, ethical hackers, and learners perform basic reconnaissance.
It combines WHOIS Lookup, Subdomain Enumeration, Directory Enumeration, and a Port Scanner (mini-Naabu) into one simple tool.

## Features

- WHOIS Lookup – get domain registration details
- Subdomain Enumeration – discover hidden subdomains using a wordlist
- Directory Enumeration – brute-force hidden directories on a target website
- Mini Naabu (Port Scanner) – quickly scan common ports of an IP
- Report Generation – all results are automatically saved to osint_report.txt


## Installation

```bash
  git clone https://github.com/Rohit-Sahani/OSINT.git
  cd OSINT-FRAMEWORK
```
## Install dependencies:

```bash
 pip install -r requirements.txt
```
## Make sure you have Python 3.8+ installed

```bash
▶️Usage
Run the script:
python osint_runner.py

```
## NOTE
```bash
Important: Make sure that all the required files and modules — including whois_lookup.py, subdomain.py, dir_enum.py, mini_naabu.py, and the wordlists (sub_wordlist.txt and dir_wordlist.txt) — are in the same folder as osint_runner.py. This ensures the framework runs correctly and can access all dependencies.

```
## Run Locally

Clone the project

```bash
git clone https://github.com/Rohit-Sahani/OSINT.git
```

Go to the project directory

```bash
cd OSINT-FRAMEWORK
```

Start the script

```bash
python osint_runner.py
```


## You will be prompted for :
```bash
Enter domain for WHOIS lookup (example.com) : 
Enter target URL for directory enumeration (https://example.com) : 
Enter subdomain wordlist file [default: sub_wordlist.txt]: 
Enter directory wordlist file [default: dir_wordlist.txt]: 
Enter IP for port scan :  

```
## Usage/Examples RUN
```bash
Enter domain for WHOIS lookup (example.com) : example.com
Enter target URL for directory enumeration (https://example.com) : https://example.com
Enter subdomain wordlist file [default: sub_wordlist.txt]: sub_wordlist.txt
Enter directory wordlist file [default: dir_wordlist.txt]: dir_wordlist.txt
Enter IP for port scan : 127.0.0.1

```
## Example Run
```bash
This video demonstrates how to use OSINT Runner. It shows entering a target domain or IP, selecting the desired modules (like WHOIS lookup, subdomain enumeration, or directory scanning), and viewing the organized results in real-time. Perfect for understanding the tool’s workflow and functionality.

```
- https://github.com/user-attachments/assets/dfd7289c-31f9-4795-8b09-c76379d28457
## PROJECT STRUCTURE
```
osint-runner/
│── osint_runner.py        # Main script
│── whois_lookup.py        # WHOIS lookup module
│── subdomain.py           # Subdomain enumeration module
│── dir_enum.py            # Directory enumeration module
│── mini_naabu.py          # Mini Naabu-style port scanner
│── sub_wordlist.txt       # Default subdomain wordlist
│── dir_wordlist.txt       # Default directory wordlist
│── requirements.txt       # Python dependencies
│── osint_report.txt       # Generated report (after run)

```

## 🛠️ Future Improvements
```
🌐 Email & phone number scraping
🌍 IP geolocation lookups
📊 Social media footprinting
🔗 API integrations for richer OSINT data
⚡ Faster enumeration & multithreading support

```
## 🤝Contributing
```bash
Contributions are always welcome!

This project is open for contributions!
Steps:
- Fork this repository
- Create a new branch (feature-newmodule)
- Commit your changes
- Push to your branch
- Create a Pull Request
- Beginners are encouraged to try modifying or adding modules — even small improvements matter!

```

## ⚠️DISCLAIMER
```bash

- This tool is for educational and ethical security testing purposes only.
- Do not use it against systems you don’t have permission to test.
- The author is not responsible for any misuse.

```
## Screenshot
```bash
The screenshot above shows OSINT Runner in action

```
- https://github.com/Rohit-Sahani/OSINT-FRAMEWORK/blob/main/Screenshot.png?raw=true


## License

This project is licensed under the MIT License - see the LICENSE file for details.



