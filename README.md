🕵️ OSINT Runner (Beginner Edition)

A beginner-friendly OSINT (Open-Source Intelligence) framework script that helps security researchers, ethical hackers, and learners perform basic reconnaissance.
It combines WHOIS Lookup, Subdomain Enumeration, Directory Enumeration, and a Port Scanner (mini-Naabu) into one simple tool.

This is just the first version — lightweight, educational, and easy to understand. Over time, it will evolve into a more advanced OSINT toolkit. Contributions are welcome! 🚀

📌 Features
✅ WHOIS Lookup – get domain registration details
✅ Subdomain Enumeration – discover hidden subdomains using a wordlist
✅ Directory Enumeration – brute-force hidden directories on a target website
✅ Mini Naabu (Port Scanner) – quickly scan common ports of an IP
✅ Report Generation – all results are automatically saved to osint_report.txt

⚙️ Installation
Clone the repository:
git clone https://github.com/yourusername/osint-runner.git
cd osint-runner

Install dependencies:
pip install -r requirements.txt


(Make sure you have Python 3.8+ installed)
▶️ Usage
Run the script:
python osint_runner.py


You will be prompted for:
A domain (for WHOIS lookup & subdomain enumeration)
A target URL (for directory enumeration)
Wordlists (default: sub_wordlist.txt, dir_wordlist.txt)
An IP address (for port scanning)


Example run:

Enter domain for WHOIS lookup (example.com) : google.com
Enter target URL for directory enumeration (https://example.com) : https://testphp.vulnweb.com
Enter subdomain wordlist file [default: sub_wordlist.txt]: 
Enter directory wordlist file [default: dir_wordlist.txt]: 
Enter IP for port scan : 192.168.1.1


Output will be shown on screen and saved in osint_report.txt.

📂 Project Structure
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

🛠️ Future Improvements
🌐 Email & phone number scraping
🌍 IP geolocation lookups
📊 Social media footprinting
🔗 API integrations for richer OSINT data
⚡ Faster enumeration & multithreading support

🤝 Contributing
This project is open for contributions!
Steps:
Fork this repository
Create a new branch (feature-newmodule)
Commit your changes
Push to your branch
Create a Pull Request

Beginners are encouraged to try modifying or adding modules — even small improvements matter!


⚠️ Disclaimer

This tool is for educational and ethical security testing purposes only.
Do not use it against systems you don’t have permission to test.
The author is not responsible for any misuse.
