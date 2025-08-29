import sys
from io import StringIO
from whois_lookup import whois_lookup
from subdomain import subdomain_finder
from dir_enum import dir_enum
from mini_naabu import scan  # my port scanner script like Nabbu

print(r"""

  ____  _________  ________
 / __ \/ __/  _/ |/ /_  __/
/ /_/ /\ \_/ //    / / /   
\____/___/___/_/|_/ /_/    
                           

""")



# File to save report
REPORT_FILE = "osint_report.txt"


# capture prints
# Tee in Python
# I needed a way to send the output of a Python program to two places simultaneously: print it on-screen, and save it to a file.
class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, data):
        for f in self.files:
            f.write(data)

    def flush(self):
        for f in self.files:
            f.flush()


def main():
    domain = input("Enter domain for WHOIS lookup (example.com) : ").strip()
    target_url = input("Enter target URL for directory enumeration (https://example.com) : ").strip()
    sub_wordlist = input("Enter subdomain wordlist file [default: sub_wordlist.txt]: ").strip() or "sub_wordlist.txt"
    dir_wordlist = input("Enter directory wordlist file [default: dir_wordlist.txt]: ").strip() or "dir_wordlist.txt"
    ip = input("Enter IP for port scan : ").strip()  

    # Open report file and redirect stdout to both terminal and file
    with open(REPORT_FILE, "w", encoding="utf-8") as f: #encoding="utf-8" → ensures the file supports all Unicode characters (like domain names with special characters).
        tee = Tee(sys.stdout, f)
        old_stdout = sys.stdout
        sys.stdout = tee

        print("\n============================")
        print("       OSINT REPORT")
        print("============================\n")

        print("[1] WHOIS Lookup")
        whois_lookup(domain)

        print("\n[2] Subdomain Enumeration")
        subdomain_finder(domain, sub_wordlist)

        print("\n[3] Directory Enumeration")
        dir_enum(target_url, dir_wordlist)

        print("\n[4] Port Scan")
        scan(ip)

        print("\n============================")
        print(f"Report saved to {REPORT_FILE}")
        print("============================\n")

        # Restore stdout
        sys.stdout = old_stdout


if __name__ == "__main__":
    main()
