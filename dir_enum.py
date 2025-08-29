import requests

def dir_enum(base_url, wordlist_file):
    with open(wordlist_file, "r") as f:
        directories = f.read().splitlines()


    print(f"Starting directory enumeration on {base_url} \n")


    for dir in directories:
        url = f"{base_url}/{dir}"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code in [200, 301, 302, 403]:
                print(f"Found : {url} (status : {r.status_code})")
        except requests.RequestException:
            pass

    
if __name__ == "__main__":
    target = input("Enter target url for directory enumeration (https://example.com) : ")
    wordlist = "dir_wordlist.txt"
    dir_enum(target, wordlist)