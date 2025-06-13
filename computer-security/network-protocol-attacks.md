---
marp: true
theme: summary
math: mathjax
---
# Network protocol attacks

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Michele Carminati's slides_)

</div>

The typical network protocol attacks are the following:
- **Denial of Service** (_against availability_): making the service unavailable to legitimate users.
- **Sniffing** (_against confidentiality_): abusive reading of network packets.
- **Spoofing** (_against integrity and authenticity_): forging network packets.

## Denial of Service attacks

### Killer packet: Ping of death

A **ping of death** is a pathological ICMP echo request that exploit a memory error in the protocol implementation. Gazillions of machines can be crashed by sending IP packets that exceed the maximum legal length (65525 octets).
The command is:
```
ping -l 65527
```
on Windows, or
```
ping -s 65527
```
on *NIX systems.

### Killer packet: Teardrop

The **teardrop** exploits a vulnerability in the TCP reassembly. It uses fragmented packets with overlapping offsets. While reassembling, the kernel can hang/crash.

### Killer packet: Land attack

A **land attack** is a packet with source IP equal to the destination IP and with SYN flag set. It could loop and lock up a TCP/IP stack.

### Flooding

A **SYN flood attack** exploits the TCP three-way handshake. The attacker generates a high volume of SYN requests with **spoofed source addresses**, without answer with an ACK to the SYN-ACK packet sent by the server. This fills the server queue with many half-open TCP/IP connections.
Thus, SYN requests from legitimate clients are dropped.

---

A **mitigation** is to use **SYN-cookies**, i.e., the server replies with a SYN-ACK but discard for the half-open connection and waits for a subsequent ACK. In the SYN-ACK packet, a SYN-cookie is added, which is the hash of several fields which identify the connection (time, source IP, source port, destination IP, destination port) and a secret. The client must respond with an ACK packet with SYN-cookie+1, which can be checked without storing anything in a queue (you just need to re-compute the hash).

### Distributed DoS with botnets

A **botnet** is a network of compromised computers, called _bots_. A **C&C** is a command-and-control infrastructure that allows the attacker (a.k.a., the botmaster) to send commands to the bots.
It has various uses, including DDoS-ing.

### Distributed DoS: Smurf

In the **smurf** attack, the attacker sends ICMP packets with a spoofed sender, corresponding to the address of the victim, to a broadcast address.

## Network-level sniffing and spoofing

Normally, a **Network Interface Card** (**NIC**) intercepts and passes to the OS only the packets directed to that host's IP. If set in **promiscuous mode**, the NIC passes to the OS any packet read off of the wire.
The difficulty of network-level sniffing changes depending on the linking device uses at layer 2. An **hub** broadcasts the traffic to every host in the broadcast domain. A **switch** selectively relays the traffic to the wire corresponding to the correct NIC.

### ARP spoofing

The **ARP** protocol maps 32 bits IPv4 addresses to 48 bits MAC addresses.
It is built around two kinds of messages:
- ARP requests: "where is 192.168.0.1"?
- ARP replies: "192.168.0.1 is at b4:e9:b0:c9:81:03".

The protocol suffers of a **lack of authentication**: it works as first come, first trusted. Thus, an attacker can forge fake replies easily.

**Possible mitigations** are:
- Check responses before trusting (if they conflict with existing addresses mappings).
- Use SEQ/ID numbers to match replies to legitimate requests.
- Employ static ARP entries where applicable.

---

#### The Content Addressable Memory (CAM) table

Switches use **CAM tables** to know/map which MAC addresses are on which physical ports. This allows to efficiently forward Ethernet frames to the correct destination.
Observe that switches are just as vulnerable to **ARP spoofing**.
In a **MAC flooding attack**, a lot of spoofed packets are generated to fill the CAM table. A full CAM table cannot cache ARP replies and must forward to every port (like a hub does). The goal of the attack is packet sniffing on switched networks.

A **mitigation** is PORT security: it limits the number of MAC addresses per port and blocks or restricts ports on suspicious behavior.

### Abusing the Spanning Tree Protocol

The **Spanning Tree Protocol** (**STP**) avoids loops on switched networks by dynamically building a spanning tree (ST). Switches decide how to build the ST by exchanging **BDPU** (bridge protocol unit data) **packets** to elect the root node. **BDPU packets are not authenticated**. This allows an attacker to send malicious BDPU claiming to be the root bridge, reshaping network topology.
The goal of the attack is forcing traffic through the attacker's device by positioning the attacker as a central forwarding point.

### IP Address Spoofing

The IP source address is **not authenticated**. Changing it in UDP or ICMP packets is easy. However, the attacker will not see the answers (e.g., they are on a different network), because they will be sent to the spoofed host (**blind spoofing**). But if the attacker is on the same network, they can sniff the rest, or use ARP spoofing.

#### TCP session hijacking

For TCP, it is not the same. TCP uses **sequence numbers** for reordering and acknowledging packets. A semi-random **Initial Sequence Number** (**ISN**) is chosen.
If a **blind spoofer** can predict the ISN, he can blindly complete the 3-way handshake without seeing the answers. However, the spoofed source should not receive the response packets, otherwise it might answer with a RST. The attacker could DoS the spoofed machine, so that it can't send the RST. This is known as **TCP session hijacking**.

### DNS cache poisoning attack

The aim of a **DNS cache poisoning attack** is to poison the cache of a non-authoritative DNS server.
It is composed of the following sequence of steps:
1. The attacker makes a **recursive query** to the victim DNS server.
2. The victim (non authoritative) DNS server contacts the authoritative server.

---

3. The attacker, **impersonating** the **authoritative** DNS server, sniffs/guess the **DNS query ID** and spoofs the answer.
4. The victim DNS server trusts and caches the malicious record (_it has been poisoned_).

After this attack has occurred, all clients that request to resolve the DN to the <u>poisoned DNS server</u> are redirected to the malicious website.

The critical point of this attack is that, in the **spoofed answer**, we need to use the **ID of the DNS query** initiated by the victim DNS server.

### DHCP poisoning attack

The **DHCP** (**Dynamic Host Configuration Protocol**) is an **unauthenticated protocol**. The attacker can intercept the DHCP requests, be the first to answer, and the client will believe that answer. With a spoofed DHCP response, the attacker can set IP addresses, DNS addresses, and the default gateway of the victim client.

### ICMP redirect

The **ICMP redirect** tells an host that  abetter route exists for a given destination, and gives the gateway for that route.
When a router detects that a host is using a non-optimal route it sends an ICMP redirect message to the host and forwards the message. The host is expected to then update its routing table.

The attacker can forge a spoofed ICMP redirect packet to re-route traffic on specific routes or to a specific host that may be not a router at all. The attack can be used to hijack traffic, or to perform a denial-of-service attack.

There is a **weak authentication** mechanism in the ICMP message: it includes the IP header and a portion of the payload (usually the first 8 bytes) of the original IP datagram. Thus, the attacker needs to intercept a packet in the "original" connection in order to forge the reply (i.e., it must be in the same network).
