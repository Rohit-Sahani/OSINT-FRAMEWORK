import dns.resolver

def subdomain_finder(domain, wordlist_file):
    
    with open(wordlist_file, "r") as f:
        subdomains = f.read().splitlines()

    print(f"Starting Domain Enumeration for {domain} ---")

    for sub in subdomains:
        url = f"{sub}.{domain}"

        # DNS using to map address record 
        # try and expect to handle error
        try:
            dns.resolver.resolve(url, "A")
            print(f"Found : {url}")
        except:
            pass

if __name__ == "__main__":
    domain = input("Enter Domain Name to find subdomains (example.com) : ")
    wordlist = "sub_wordlist.txt"
    subdomain_finder(domain, wordlist)