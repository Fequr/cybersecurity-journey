Network Checker

A simple Python tool for checking basic network connectivity.

This project is part of my cybersecurity learning journey. It helps me practice Python programming and understand fundamental networking concepts.

Features

* DNS Lookup — resolves a domain name to an IPv4 address.
* Ping Test — checks whether a host responds to ICMP requests and displays ping statistics.
* HTTP/HTTPS Check — sends an HTTPS request and displays the HTTP status code and final URL.
* Error Handling — handles invalid domains, connection errors, and timeouts.

Technologies

* Python 3
* socket
* subprocess
* urllib

All libraries used by this project are included in the Python standard library.

Requirements

* Python 3
* macOS or Linux

The current implementation uses the ping -c 4 command, which is compatible with macOS and Linux.

Usage

Clone the repository:

git clone https://github.com/Fequr/cybersecurity-journey.git

Navigate to the project directory:

cd cybersecurity-journey

Run the program:

python3 projects/network-checker/main.py

Enter a domain when prompted, for example:

github.com

The program will perform DNS lookup, ping, and HTTPS checks.

Example Output

DNS lookup successful!
Domain: github.com
IPv4 address: 140.82.121.4
Pinging github.com...
Ping successful!
Checking HTTP/HTTPS: https://github.com
HTTP check successful!
Status code: 200
Final URL: https://github.com

Actual IP addresses, response times, and HTTP status codes may vary.

Learning Goals

* Understand DNS resolution and IPv4 addresses.
* Learn the basics of ICMP and ping.
* Understand HTTP status codes and HTTPS requests.
* Practice Python functions and exception handling.
* Learn Git and GitHub workflows.

Limitations

* DNS lookup currently returns one IPv4 address.
* A failed ping does not necessarily mean that a website is unavailable.
* The HTTP check tests HTTPS only.
* Some servers may block ping requests or respond differently to HEAD requests.
* Results depend on the local network and the target server.

Disclaimer

This project is intended for educational purposes and basic connectivity troubleshooting. It does not perform vulnerability scanning or penetration testing.