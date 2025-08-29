import whois

def whois_lookup(domain):
    try : 
        print(f"Fetching WHOIS info for : {domain}")
        w = whois.whois(domain)

        print("--- WHOIS information ---")
        print(f"Domain name : {w.domain_name}")
        print(f"Registrar : {w.registrar}")
        print(f"Creation Date : {w.creation_date}")
        print(f"Expiration : {w.expiration_date}")
        print(f"Name Servers : {w.name_servers}")
        print(f"Emails : {w.Emails}")
        print(f"Country : {w.country}")

    except Exception as e:
        print(f" [-] Error : {e}")


if __name__ == "__main__":
    domain = input("Enter Domain name for WHOIS lookup : (example.com)").strip()
    whois_lookup(domain)

