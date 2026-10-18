Day 01 — Networking Fundamentals

1. IP Address

An IP address identifies a network interface and allows devices to communicate over an IP network.

There are two main versions:

* IPv4: For example, 192.168.1.1.
* IPv6: For example, 2001:db8::1.

2. DNS (Domain Name System)

DNS translates domain names into DNS records, including IP addresses.

It allows users to access websites using names such as google.com instead of remembering their IP addresses.

Command:

nslookup google.com

My result:

Server: 10.254.254.254
Address: 10.254.254.254#53
Name: google.com
Address: 142.251.38.110

What I learned:

* My computer queried the DNS server at 10.254.254.254.
* The DNS response contained the IPv4 address 142.251.38.110.
* Port 53 is the standard DNS port.
* Non-authoritative answer means the response came from a server that is not authoritative for that domain.

3. ICMP and Ping

ICMP (Internet Control Message Protocol) is used for network diagnostics and reporting certain network errors.

The ping utility commonly uses ICMP Echo Request and Echo Reply messages to check whether a destination responds.

Command:

ping -c 4 google.com

On macOS, -c 4 sends four requests.

My result:

4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 35.617/44.674/69.535/14.365 ms

What I learned:

* All four requests received replies.
* Packet loss was 0%.
* Average round-trip time was approximately 44.674 ms.
* A failed ping does not necessarily mean that a server is offline, because ICMP traffic may be blocked.

4. TTL (Time To Live)

TTL limits how many network hops an IP packet can pass through before being discarded.

Each router forwarding an IPv4 packet decreases its TTL by at least one. When it reaches zero, the packet is discarded.

Example from my ping output:

ttl=119

This is the TTL value in the received packet. Without knowing its initial value, I cannot determine the exact number of hops from this number alone.

5. Latency

Latency is the time required for data to travel between two points. It is commonly measured in milliseconds (ms).

The ping utility reports round-trip time: the time for a request to reach its destination and for a reply to return.

Common measurements:

* min — minimum round-trip time.
* avg — average round-trip time.
* max — maximum round-trip time.
* stddev — standard deviation of the measured times.

My average round-trip time to Google was approximately 44.674 ms.

Latency can be affected by network congestion, routing, physical distance, and server performance.

6. HTTP and HTTPS

HTTP (Hypertext Transfer Protocol) is an application-layer protocol used for communication between web clients and servers.

An HTTP response includes a status code and headers. It may also contain a response body.

Common status codes:

* 200 OK — the request succeeded.
* 301 Moved Permanently — the resource has been permanently redirected.
* 403 Forbidden — the server refuses to fulfill the request.
* 404 Not Found — the requested resource was not found.
* 500 Internal Server Error — the server encountered an unexpected problem.

HTTPS is HTTP protected by TLS, which provides encryption and helps authenticate the server.

Command:

curl -I https://google.com

The -I option requests response headers without downloading the response body.

7. Traceroute

Traceroute is a network diagnostic utility that attempts to identify the routers along the route to a destination.

Command on macOS:

traceroute google.com

It displays network hops and their response times.

An output of * * * means that the probes did not receive responses within the timeout. Some routers filter or ignore traceroute probes, so this does not automatically indicate a network failure.

8. Commands Practiced

Command	Purpose
ping -c 4 google.com	Check whether a destination responds to ping requests
nslookup google.com	Query DNS information for a domain
traceroute google.com	Investigate the route to a destination
curl -I https://google.com	Request HTTP response headers

Key Takeaways

* IP addresses allow devices to communicate over IP networks.
* DNS resolves domain names into DNS records, including IP addresses.
* ICMP supports network diagnostics.
* TTL limits the number of hops an IP packet can pass through.
* Latency measures network response time.
* HTTP and HTTPS are used for communication between web clients and servers.
* Network diagnostic tools help investigate connectivity and DNS resolution.

Next Steps

* Learn the differences between TCP and UDP.
* Understand ports and client-server communication.
* Practice inspecting HTTP requests and responses.