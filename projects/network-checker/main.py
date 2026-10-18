import socket
import subprocess
import urllib.request
import urllib.error

def dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)

        print("\nDNS lookup successful!")
        print(f"Domain: {domain}")
        print(f"IPv4 address: {ip_address}")

    except socket.gaierror:
        print(f"\nDNS lookup failed for: {domain}")
        print("Check the domain name or your network connection.")

def ping_test(domain):
    print(f"\nPinging {domain}...")

    try:

        result = subprocess.run(
            ["ping", "-c", "4", domain],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print("Ping successful!")

        else:
            print("Ping failed.")

        print(result.stdout)

        if result.stderr:
            print("Error details:", result.stderr)

    except subprocess.TimeoutExpired:
        print("Ping timed out after 10 seconds.")

    except OSError as error:
        print(f"Could not run ping: {error}")

def http_check(domain):
    url = f"https://{domain}"

    print(f"\nChecking HTTP/HTTPS: {url}")
    try:
        request = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "NetworkChecker/1.0"}
        )
        
        with urllib.request.urlopen(request, timeout=10) as response:
            print("HTTP check successful!")
            print(f"Status code: {response.status}")
            print(f"Final URL: {response.url}")

    except urllib.error.HTTPError as error:
        print(f"HTTP error: {error.code}")

    except urllib.error.URLError as error:
        print(f"Connection failed: {error.reason}")

    except TimeoutError:
        print("HTTP request timed out.")

    except OSError as error:
        print(f"Network error: {error}")

def main():
    domain = input("Enter a domain (e.g. github.com): ").strip()

    if not domain:
        print("Error: domain cannot be empty.")
        return
    dns_lookup(domain)
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        print("\nCannot continue: domain could not be resolved.")
        return
    ping_test(domain)
    http_check(domain)

if __name__ == "__main__":
    main()